import collections

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
  import generate_metaworld_scene_dataset
except ImportError:
  import sys
  sys.append('src')
  import generate_metaworld_scene_dataset

import embed_prompt

class ConditionEvaluator(nn.Module):

  def setup(self):
    self.cond_encoder = nn.Sequential([
        nn.Dense(256),
        nn.relu,
        nn.Dense(256),
        nn.relu,
        nn.Dense(256),
        nn.relu,
        nn.Dense(128),
        nn.relu,
        nn.Dense(64),
        nn.relu,
        nn.Dense(64),
    ])
    self.state_encoder = nn.Sequential([
        nn.Dense(128),
        nn.relu,
        nn.Dense(128),
        nn.relu,
        nn.Dense(128),
        nn.relu,
        nn.Dense(128),
        nn.relu,
        nn.Dense(64),
        nn.relu,
        nn.Dense(64),
    ])

  def __call__(self, low_dim, conditions):
    conditions_enc = self.cond_encoder(conditions)
    state_enc = self.state_encoder(low_dim)
    result = jnp.einsum('ijk,ik->ij', conditions_enc, state_enc)
    return result

@jax.jit
def update_model(state, grads):
  return state.apply_gradients(grads=grads)

@jax.jit
def apply_model(state, observations, descriptors_embedded, targets):
  def loss_fn(params):
    truth_values = state.apply_fn(params, observations, descriptors_embedded)
    loss = -jnp.mean(truth_values * targets) / (1 + jnp.sum(targets != 0))
    # loss = jnp.mean(optax.l2_loss(truth_values, targets))
    return loss, truth_values

  grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
  (loss, truth_values), grads = grad_fn(state.params)
  accuracy = jnp.sum(truth_values * targets > 0) / jnp.sum(targets != 0)
  return grads, loss, accuracy


class CondAgent(nn.Module):

  def setup(self):
    with open('data/embedded_mt10.pkl', 'rb') as f:
      plans = pickle.load(f)
    parsed_plans = {}
    for (plan_name, plan) in plans.items():
      conds = jnp.concatenate([step['cond_embed'] for step in plan])
      actions = jnp.concatenate([step['action_embed'] for step in plan])
      parsed_plans[plan_name] = {
          'conds': conds,
          'actions': actions,
      }


def store_obs(env_name, client, observation):
  client.insert(pickle.dumps({
      'observation': observation,
      'descriptors': generate_metaworld_scene_dataset.describe_obs(env_name, observation)
  }), priorities={'mt_obs': 1.})

ENV_CACHE = collections.defaultdict(list)

def make_env(env_name, seed: int):
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
    env.seeded_rand_vec = True
    return env

CLIENT = None

def sample_process(env_name: str, port: int, seed: int):
  random_policy_prob=0.005
  global CLIENT
  client = CLIENT or reverb.Client(f'localhost:{port}')
  CLIENT = client

  try:
    # This operation is atomic!
    # Important for multithreading!
    env = ENV_CACHE[env_name].pop()
  except IndexError:
    env = make_env(env_name, seed)

  max_episode_length = 500
  policy = SawyerUniversalV2Policy(env_name=env_name)
  observation = env.reset()
  use_random = False
  for i in range(max_episode_length):
    store_obs(env_name, client, observation)
    if i > 0 and not use_random and np.random.uniform() < random_policy_prob:
      use_random = True
    if use_random:
      noise = env.action_space.sample()
      alpha = 0.9
      action = alpha * action + (1 - alpha) * noise
    else:
      action = policy.get_action(observation)
    observation, r, done, info = env.step(action)
  store_obs(env_name, client, observation)
  ENV_CACHE[env_name].append(env)

DISC_DIM = 512

def train_epoch(state, batch):
  observations = []
  descriptor_names = []
  descriptors_embeddings = []
  descriptors_targets = []
  for sample_pkl in batch:
    sample = pickle.loads(sample_pkl[0].data[0].item())
    descriptors_text = list(sample['descriptors'].keys())
    descriptors_embedded = [embed_prompt.embed_condition(text)
                            for text in descriptors_text]
    targets = [sample['descriptors'][text]
               for text in descriptors_text]
    observations.append(sample['observation'])
    descriptors_embeddings.append(descriptors_embedded)
    descriptors_targets.append(targets)
  obs_batch = np.stack(observations)
  assert len(obs_batch.shape) == 2
  assert obs_batch.shape[0] == len(descriptors_embeddings)
  pad_cond_dim = max(len(discs) for discs in descriptors_embeddings)
  descriptors_padded = np.zeros([obs_batch.shape[0], pad_cond_dim, DISC_DIM])
  targets_padded = np.zeros([obs_batch.shape[0], pad_cond_dim])
  for i in range(len(descriptors_embeddings)):
    for j in range(len(descriptors_embeddings[i])):
      descriptors_padded[i][j] = descriptors_embeddings[i][j]
      targets_padded[i][j] = descriptors_targets[i][j]

  grads, loss, accuracy = apply_model(state, obs_batch, descriptors_padded,
                                      targets_padded)
  state = update_model(state, grads)
  return state, loss, accuracy

def train_and_evaluate(envs=','.join([e[:-3] for e in MT10_V2.keys()]), seed=random.randrange(1000),
                       num_batches=1e5, batch_size=16):
  workdir = f'data/train_evaluator_seed={seed}'
  rng = jax.random.PRNGKey(seed)
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams(dict(locals()))

  env_names = list(envs.split(','))
  max_episode_length = 500
  max_size = len(env_names) * max_episode_length * 10
  server = generate_metaworld_scene_dataset.start_reverb_server(max_size=max_size)
  client = reverb.Client(f'localhost:{server.port}')

  rng, init_rng = jax.random.split(rng)
  learning_rate = 1e-6
  momentum = 0.99
  cond_evaluator = ConditionEvaluator()
  params = cond_evaluator.init(rng, jnp.ones([batch_size, 39]), jnp.ones([batch_size, 3, DISC_DIM]))
  tx = optax.sgd(learning_rate, momentum)
  state = train_state.TrainState.create(
      apply_fn=cond_evaluator.apply, params=params, tx=tx)

  with concurrent.futures.ThreadPoolExecutor() as executor:
    for epoch in tqdm(range(int(num_batches))):
      # We need new samples
      if epoch % (len(env_names) * max_episode_length / batch_size) == 0:
        concurrent.futures.wait([
          executor.submit(sample_process, env_name, server.port, seed)
          for env_name in env_names])
        with open(f'{workdir}/{epoch}.pkl', 'wb') as f:
          pickle.dump(state.params, f)

      batch = client.sample('mt_obs', num_samples = batch_size)
      state, train_loss, train_accuracy = train_epoch(state, batch)

      summary_writer.scalar('train_loss', train_loss, epoch)
      summary_writer.scalar('train_accuracy', train_accuracy, epoch)

      summary_writer.flush()
  return state

if __name__ == '__main__':
  train_and_evaluate()
