import collections

import clize
import os
from pprint import pprint
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

import easy_process
from sample_utils import make_env, sample_noisy_policy, MT10_ENV_NAMES

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
    # loss = -jnp.mean(truth_values * targets) / (1 + jnp.sum(targets != 0))
    loss = jnp.mean(optax.l2_loss(truth_values, targets))
    return loss, truth_values

  grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
  (loss, truth_values), grads = grad_fn(state.params)
  accuracy = jnp.sum(truth_values * targets > 0) / jnp.sum(targets != 0)
  return grads, loss, accuracy


def store_obs(env_name, client, observation):
  client.insert(pickle.dumps({
      'observation': observation,
      'descriptors': generate_metaworld_scene_dataset.describe_obs(env_name, observation)
  }), priorities={'mt_obs': 1.})

ENV_CACHE = collections.defaultdict(list)

CLIENT = None

@easy_process.subprocess_func
def sample_process(*, env_name: str, noise_scale: float, seed: int, parent):
  env = make_env(env_name, seed)
  policy = SawyerUniversalV2Policy(env_name=env_name)

  while True:
    parent.sendrecv(list(sample_noisy_policy(env, policy, noise_scale)))


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

def worker_dataset(*, envs=','.join(MT10_ENV_NAMES),
                   n_timesteps=1000, seed=100, noise_scale=0.1):
  env_names = list(envs.split(','))
  with easy_process.Scope():
    workers = [sample_process(env_name=env_name, seed=seed, noise_scale=noise_scale)
              for env_name in env_names]
    datapoints = []
    with tqdm(total=n_timesteps) as pbar:
      while len(datapoints) < n_timesteps:
        for worker in workers:
          worker.send('gather', block=False)
        for worker in workers:
          episode = worker.recv(block=False)
          if episode:
            datapoints.extend(episode)
            pbar.update(len(episode))
  return datapoints


def train_and_evaluate(envs=','.join([e[:-3] for e in MT10_V2.keys()]),
                       seed=random.randrange(1000),
                       num_batches=1e4, batch_size=16):
  workdir = f'~/data/train_evaluator_seed={seed}'
  rng = jax.random.PRNGKey(seed)
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams(dict(locals()))

  env_names = list(envs.split(','))
  max_episode_length = 500
  max_size = len(env_names) * max_episode_length * 10
  server = generate_metaworld_scene_dataset.start_reverb_server(max_size=max_size)
  client = reverb.Client(f'localhost:{server.port}')

  rng, init_rng = jax.random.split(rng)
  learning_rate = 1e-4
  momentum = 0.99
  cond_evaluator = ConditionEvaluator()
  params = cond_evaluator.init(rng, jnp.ones([batch_size, 39]),
                               jnp.ones([batch_size, 3, DISC_DIM]))
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
  # pprint(worker_dataset(MT10_ENV_NAMES, 50000, seed=100)[100])
  clize.run(worker_dataset)
