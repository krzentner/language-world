import collections
from dataclasses import dataclass
import clize
from functools import partial

import random
from absl import logging
from flax import linen as nn
from flax.metrics import tensorboard
from flax.training import train_state
import jax
import jax.numpy as jnp
import ml_collections
import numpy as np
import optax
import pickle
import reverb
import concurrent.futures

from tqdm import tqdm
from metaworld.envs.mujoco.env_dict import MT10_V2
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE

try:
  import train_evaluator
except ImportError:
  import sys
  sys.append('src')
  import train_evaluator

import generate_metaworld_scene_dataset
import embed_prompt
import metaworld_jax_controllers
import easy_process

import pickle

ENV_NAME_TO_PLAN_NAME = {
    'drawer-close': 'close_drawer',
    'drawer-open': 'open_drawer',
    'peg-insert-side': 'insert_peg_right_into_slot',
    'door-open': 'open_door',
    'pick-place': 'pick_puck_and_hold_at_target',
    'button-press-topdown': 'press_button_from_above',
    'push': 'slide_puck_to_target',
    'window-close': 'slide_window_closed_right',
    'window-open': 'slide_window_open_left',
    'reach': 'reach_for_target',
}

def pad_list(seq, max_len=None):
  if max_len is None:
    max_len = max(len(s) for s in seq)
  zero = jnp.zeros(seq[0][0].shape)
  padded = jnp.array([[s[i] if len(s) > i else zero
                       for i in range(max_len)]
                      for s in seq])
  mask = jnp.array([[1 if len(s) > i else 0
                     for i in range(max_len)]
                    for s in seq])
  return padded, mask

class CondAgent(nn.Module):

  def setup(self):
    with open('data/embedded_mt10.pkl', 'rb') as f:
      plans = pickle.load(f)
    parsed_plans = {}
    for (plan_name, plan) in plans.items():
      conds = jnp.concatenate([step['cond_embed'] for step in plan])
      actions = jnp.concatenate([step['action_embed'] for step in plan])
      parsed_plans[plan_name] = {
          'conds': self.param(f'{plan_name}.conds', lambda _: conds),
          'actions': self.param(f'{plan_name}.actions', lambda _: actions),
      }
    self.plans = parsed_plans
    self.cond_evaluator = train_evaluator.ConditionEvaluator()
    self.controllers = {}

  def __call__(self, env_names, low_dim):
    plans = [self.plans[ENV_NAME_TO_PLAN_NAME[env_name]]
             for env_name in env_names]
    conds_padded, conds_mask = pad_list([plan['conds'] for plan in plans])
    conds_truth_values = self.cond_evaluator(low_dim, conds_padded)
    actions_padded, actions_mask = pad_list([plan['actions'] for plan in plans])
    action = jnp.einsum('ikj,ik->ij',
                        actions_padded,
                        nn.softmax(conds_truth_values,
                                   where=conds_mask,
                                   initial=0))
    controller_names = []
    controller_names_embedded = []
    controller_outputs = []
    for (env, obs) in zip(env_names, low_dim):
      parsed_obs = metaworld_jax_controllers.parse_obs(obs)
      control_out = []
      control_names = []
      control_names_emb = []
      for (name, controller) in metaworld_jax_controllers.CONTROLLERS.items():
        if controller['env-name'] != env:
          continue
        control_names.append(name)
        control_names_emb.append(embed_prompt.embed_action(name))
        control_out.append(metaworld_jax_controllers.run_controller(name, parsed_obs))
      controller_names.append(control_names)
      controller_names_embedded.append(control_names_emb)
      controller_outputs.append(control_out)
    assert controller_names_embedded
    names_padded, names_mask = pad_list(controller_names_embedded)
    controller_weights = nn.softmax(jnp.einsum('ik,ijk->ij', action, names_padded),
                                    where=names_mask,
                                    initial=0)
    outputs_padded, output_mask = pad_list(controller_outputs)
    output = jnp.einsum('ij,ijk->ik', controller_weights, outputs_padded)
    return output

  def as_policy(self, env_name, state):
    return CondAgentPolicy(cond_agent=self, env_name=env_name, state=state)

@dataclass
class CondAgentPolicy:

  cond_agent: CondAgent
  state: train_state.TrainState
  env_name: str or None

  def get_action(self, low_dim, env_name=None):
    env_name = env_name or self.env_name
    assert env_name
    return np.asarray(self.state.apply_fn(self.state.params,
                                          [self.env_name], [low_dim]))[0]

  def get_actions(self, observations, env_names):
    return np.asarray(self.state.apply_fn(self.state.params,
                                          env_names, observations))


@partial(jax.jit, static_argnames=['env_names'])
def step_agent(state, env_names, observations):
    return state.apply_fn(state.params, env_names, observations)

@jax.jit
def update_model(state, grads):
  return state.apply_gradients(grads=grads)

# @partial(jax.jit, static_argnames=['env_names'])
def apply_model(state, env_names, observations, action_targets):
  def loss_fn(params):
    action = state.apply_fn(params, env_names, observations)
    loss = jnp.mean(optax.l2_loss(action, action_targets))
    return loss

  grad_fn = jax.value_and_grad(loss_fn)
  loss, grads = grad_fn(state.params)
  return grads, loss

def train_epoch(state, batch):
  observations = []
  action_targets = []
  env_names = []
  for sample_pkl in batch:
    sample = pickle.loads(sample_pkl[0].data[0].item())
    observations.append(sample['observation'])
    action_targets.append(sample['action'])
    env_names.append(sample['env_name'])
  obs_batch = np.stack(observations)
  action_batch = np.stack(action_targets)
  grads, loss = apply_model(state, tuple(env_names), obs_batch, action_batch)
  state = update_model(state, grads)
  return state, loss


ENV_CACHE = collections.defaultdict(list)

def make_env(env_name, seed: int):
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
    env.seeded_rand_vec = True
    return env

def get_env(env_name, seed):
  try:
    # This operation is atomic!
    # Important for multithreading!
    env = ENV_CACHE[env_name].pop()
  except IndexError:
    env = make_env(env_name, seed)
  return env

def return_env(env_name, env):
  ENV_CACHE[env_name].append(env)

def store(env_name, client, observation, action, reward):
  client.insert(pickle.dumps({
      'env_name': env_name,
      'observation': observation,
      'action': action,
      'reward': reward,
  }), priorities={'mt_obs': 1.})

CLIENT = None

def sample_process(env_name: str, port: int, seed: int, noise_scale: float):
  global CLIENT
  client = CLIENT or reverb.Client(f'localhost:{port}')
  CLIENT = client

  env = get_env(env_name, seed)
  max_episode_length = 500
  policy = SawyerUniversalV2Policy(env_name=env_name)
  observation = env.reset()
  use_random = False
  for i in tqdm(range(max_episode_length)):
    action = policy.get_action(observation)
    action_noisy = action + np.random.normal(scale=noise_scale)
    observation, reward, done, info = env.step(action_noisy)
    store(env_name, client, observation, action, reward)
  return_env(env_name, env)

@easy_process.subprocess_func
def sampler_proc(env_name, port, seed, noise_scale, *, parent):
  client = reverb.Client(f'localhost:{port}')

  while True:
    print('waiting')
    msg = parent.recv()
    if msg == 'stop':
      return
    elif msg == 'gather':
      try:
        env = get_env(env_name, seed)
        max_episode_length = 500
        policy = SawyerUniversalV2Policy(env_name=env_name)
        observation = env.reset()
        use_random = False
        for i in tqdm(range(max_episode_length)):
          print(i)
          action = policy.get_action(observation)
          action_noisy = action + np.random.normal(scale=noise_scale)
          observation, reward, done, info = env.step(action_noisy)
          store(env_name, client, observation, action, reward)
        return_env(env_name, env)
      except Exception as ex:
        print(ex)
      parent.send('gather done')
    else:
      raise TypeError("Unknown message")


def eval_policy(policy, env_names, seed):
  env_names = tuple(env_names)
  envs = [get_env(name, seed) for name in env_names]

  max_episode_length = 500
  observations = [env.reset() for env in envs]
  use_random = False
  rewards = {name: [] for name in env_names}
  for i in tqdm(range(max_episode_length)):
    actions = step_agent(policy.state, env_names, jnp.array(observations))
    for i, action in enumerate(actions):
      observations[i], reward, done, info = envs[i].step(np.array(action))
      rewards[env_names[i]].append(reward)

  for (env_name, env) in zip(env_names, envs):
    return_env(env_name, env)
  return rewards


def train_and_evaluate(train_envs=','.join([e[:-3] for e in MT10_V2.keys()]),
                       test_envs='',
                       # test_envs=','.join([e[:-3] for e in MT10_V2.keys()]),
                       seed=random.randrange(1000),
                       num_batches=1e6, batch_size=16, noise_scale=0.1):
  workdir = f'~/data/evaluator_agent_seed={seed}_noise-scale={noise_scale}'
  rng = jax.random.PRNGKey(seed)
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams(dict(locals()))

  train_env_names = [name for name in train_envs.split(',') if name]
  test_env_names = [name for name in test_envs.split(',') if name]
  max_episode_length = 500
  max_size = len(train_env_names) * max_episode_length * 10
  server = generate_metaworld_scene_dataset.start_reverb_server(max_size=max_size)
  client = reverb.Client(f'localhost:{server.port}')

  rng, init_rng = jax.random.split(rng)
  learning_rate = 1e-4
  momentum = 0.99
  cond_agent = CondAgent()
  params = cond_agent.init(rng, ['drawer-close', 'pick-place'] * int(batch_size / 2),
                           jnp.ones([batch_size, 39]))
  with open('~/data/best_evaluator.pkl', 'rb') as f:
    cond_eval_state = pickle.load(f)
  params = params.copy({'cond_evaluator': cond_eval_state['params']})
  tx = optax.sgd(learning_rate, momentum)
  state = train_state.TrainState.create(
      apply_fn=cond_agent.apply, params=params, tx=tx)

  workers = [sampler_proc(env_name, server.port, seed, noise_scale)
             for env_name in train_env_names]

  for epoch in tqdm(range(int(num_batches))):
    # We need new samples
    if epoch % 100 == 0:
      for worker in workers:
        worker.send('gather', block=True)
      for worker in workers:
        worker.recv()
      with open(f'{workdir}/{epoch}.pkl', 'wb') as f:
        pickle.dump(state.params, f)

    if epoch % 100 == 0:
      rewards = eval_policy(cond_agent.as_policy(None, state),
                            train_env_names + test_env_names,
                            seed)

      avg_rewards = []
      for env_name in train_env_names:
        avg_reward = np.mean(rewards[env_name])
        summary_writer.scalar(f'{env_name}/avg_reward', avg_reward, epoch)
        avg_rewards.append(avg_reward)
      summary_writer.scalar('train_envs/avg_reward', np.mean(avg_rewards), epoch)

      avg_rewards = []
      for env_name in test_env_names:
        avg_reward = np.mean(rewards[env_name])
        summary_writer.scalar(f'{env_name}/avg_reward', avg_reward, epoch)
        avg_rewards.append(avg_reward)
      summary_writer.scalar('test_envs/avg_reward', np.mean(avg_rewards), epoch)

    batch = client.sample('mt_obs', num_samples = batch_size)
    state, train_loss = train_epoch(state, batch)

    summary_writer.scalar('train_loss', train_loss, epoch)

    summary_writer.flush()
    with open(f'{workdir}/checkpoint.pkl', 'wb') as f:
      pickle.dump(state.params, f)
  return state

if __name__ == '__main__':
  clize.run(train_and_evaluate)
