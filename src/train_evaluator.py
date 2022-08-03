import collections

import clize
import os
from pprint import pprint
import random
from flax import linen as nn
from flax.metrics import tensorboard
from flax.training import train_state
import jax
import jax.numpy as jnp
import ml_collections
import numpy as np
import optax
import pickle
from tqdm import tqdm

import easy_process
from sample_utils import (make_env, MT50_ENV_NAMES,
                          sample_policy_with_noise_process)
from run_utils import float_list, str_list
from ou_process import OUProcess
import jax_utils
from generate_metaworld_scene_dataset import describe_obs
from metaworld_universal_policy import SawyerUniversalV2Policy
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
def apply_model(state, low_dim, conditions, targets):
  def loss_fn(params):
    truth_values = state.apply_fn(params, low_dim, conditions)
    loss = jnp.mean(optax.sigmoid_binary_cross_entropy(
        jnp.stack([truth_values, -truth_values], axis=-1),
        jnp.stack([targets, 1 - targets], axis=-1)))
    return loss, truth_values

  grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
  (loss, truth_values), grads = grad_fn(state.params)
  accuracy = jnp.mean(targets * (truth_values > 0) +
                      (1 - targets) * (truth_values < 0))
  return grads, loss, {'accuracy': accuracy,
                       'mean_truth_value': jnp.mean(truth_values),
                       'var_truth_value': jnp.var(truth_values),
                       'mean_abs_truth_values': jnp.mean(jnp.abs(truth_values))}


@easy_process.subprocess_func
def sample_process(*, env_name: str, noise_scales: [float], seed: int, parent):
  env = make_env(env_name, seed)
  policy = SawyerUniversalV2Policy(env_name=env_name)

  while True:
    random.shuffle(noise_scales)
    for noise_scale in noise_scales:
      ou_proc = OUProcess(dimensions=env.action_space.shape[0],
                          sigma=noise_scale)
      episode = []
      for data in sample_policy_with_noise_process(env, policy, ou_proc):
        data['env_name'] = env_name
        data['noise_scale'] = noise_scale
        episode.append(data)
      parent.sendrecv(episode)


DISC_DIM = 512

def worker_dataset(*,
                   envs: str_list=MT50_ENV_NAMES,
                   n_timesteps=1000, seed=jax_utils.DEFAULT_SEED,
                   noise_scales: float_list=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]):
  with easy_process.Scope():
    workers = [sample_process(env_name=env_name, seed=seed, noise_scales=noise_scales)
              for env_name in envs]
    datapoints = []
    with tqdm(total=n_timesteps) as pbar:
      while len(datapoints) < n_timesteps:
        for worker in workers:
          episode = worker.recv(block=False)
          if episode:
            datapoints.extend(episode)
            pbar.update(len(episode))
  return datapoints


def preprocess(batch):
  observations = []
  descriptor_names = []
  descriptors_embeddings = []
  descriptors_targets = []
  for data in batch:
    observation = data['observation']
    env_name = data['env_name']
    descriptors = describe_obs(env_name, observation)
    descriptors_text = list(descriptors.keys())
    random.shuffle(descriptors_text)
    descriptors_text = descriptors_text[:256]
    descriptors_embedded = [embed_prompt.embed_condition(text)
                            for text in descriptors_text]
    targets = [descriptors[text]
               for text in descriptors_text]
    observations.append(observation)
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
  return (obs_batch, descriptors_padded), targets_padded

def train_evaluator(*, envs: str_list=MT50_ENV_NAMES,
                    n_epochs=50, n_timesteps=int(1e7), seed=jax_utils.DEFAULT_SEED,
                    noise_scales: float_list=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]):
  print('Gathering dataset:')
  data = worker_dataset(envs=envs, n_timesteps=n_timesteps, seed=seed,
                        noise_scales=noise_scales)
  cond_evaluator = ConditionEvaluator()
  jax_utils.fit_model(cond_evaluator, data, apply_model, 'evaluator',
                      batch_size=4, preprocess=preprocess, seed=seed)
  embed_prompt.save_cache()


if __name__ == '__main__':
  clize.run(train_evaluator)
