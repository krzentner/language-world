import shutil as sh

import tensorflow as tf
import numpy as np
import clize
from tqdm import tqdm

from metaworld.envs.mujoco.env_dict import MT10_V2
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE

import reverb

REVERB_CHECKPOINT_FILENAME = 'data/reverb_checkpoint'

def describe_relative_coordinates(xyz1, xyz2):
  descriptors = {
      "around": 0,
      "near": 0,
      "right of": 0,
      "left of": 0,
      "behind": 0,
      "in front of": 0,
      "above": 0,
      "below": 0,
  }
  if np.linalg.norm(xyz1 - xyz2) < .04:
    descriptors["around"] = 1.
    descriptors["near"] = 1.
  if xyz1[0] - xyz2[0] > 0.04:
    descriptors["right of"] = 1.
  if xyz1[0] - xyz2[0] < -0.04:
    descriptors["left of"] = 1.
  if (xyz1[1] - xyz2[1] > 0.04 and np.linalg.norm(xyz1[[0,2]] - xyz2[[0, 2]]) < 0.04):
    descriptors["behind"] = 1.
  if (xyz1[1] - xyz2[1] < -0.04 and np.linalg.norm(xyz1[[0,2]] - xyz2[[0, 2]]) < 0.04):
    descriptors["in front of"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] > 0.04:
    descriptors["above"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] < -0.04:
    descriptors["below"] = 1.
  for key in list(descriptors.keys()):
    descriptors[f"not {key}"] = -descriptors[key]
  return descriptors

OBJECT_NAMES = {
    'drawer-open': {
        'obj1_pos': "drawer handle",
    },
    'drawer-close': {
        'obj1_pos': "drawer handle",
    },
    'peg-insert-side': {
        'obj1_pos': "peg",
        'goal_pos': "hole",
    },
    'reach': {
        'goal_pos': "reach target"
    },
    'window-open': {
        'obj1_pos': "window handle",
    },
    'window-close': {
        'obj1_pos': "window handle",
    },
    'door-open': {
        'obj1_pos': "door handle"
    },
    'push': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'pick-place': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'button-press-topdown': {
        'obj1_pos': "button",
    }
}

def describe_obs(env_name, low_dim):
  o_d = parse_obs(low_dim)
  keys_to_names = {'hand_pos': "the robot's gripper"}
  keys_to_names.update(OBJECT_NAMES[env_name])
  descriptors = {}
  for (key1, name1) in keys_to_names.items():
    for (key2, name2) in keys_to_names.items():
      if key1 == key2:
        continue
      disc = describe_relative_coordinates(o_d[key1], o_d[key2])
      for (key, val) in disc.items():
        descriptors[f"{name1} is {key} {name2}"] = val
  return descriptors


def store_obs(client, observation):
  client.insert(observation, priorities={'mt_obs': 1.})

def start_reverb_server(max_size, checkpointer=None):
  return reverb.Server(tables=[
      reverb.Table(
          name='mt_obs',
          sampler=reverb.selectors.Uniform(),
          remover=reverb.selectors.Fifo(),
          max_size=max_size,
          rate_limiter=reverb.rate_limiters.MinSize(1)),
      ],
      checkpointer=checkpointer,
  )

def generate(n_episodes_per_env=100, random_policy_prob=0.005,
             envs=','.join([e[:-3] for e in MT10_V2.keys()]), seed=100):
  env_names = list(envs.split(','))
  max_episode_length = 500
  max_size = len(env_names) * n_episodes_per_env * max_episode_length
  server = start_reverb_server(max_size=max_size)
  client = reverb.Client(f'localhost:{server.port}')

  for env_name in env_names:
    print('Gathering', env_name, '...')
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
    env.seeded_rand_vec = True
    policy = SawyerUniversalV2Policy(env_name=env_name)
    for episode in tqdm(range(n_episodes_per_env)):
      observation = env.reset()
      use_random = False
      for i in range(max_episode_length):
        store_obs(client, observation)
        if i > 0 and not use_random and np.random.uniform() < random_policy_prob:
          # print('switched to random on step', i)
          use_random = True
        if use_random:
          noise = env.action_space.sample()
          alpha = 0.9
          action = alpha * action + (1 - alpha) * noise
        else:
          action = policy.get_action(observation)
        observation, r, done, info = env.step(action)
      store_obs(client, observation)
  checkpoint_file = client.checkpoint()
  sh.copytree(checkpoint_file, REVERB_CHECKPOINT_FILENAME)
  print('Saving checkpoint to:', REVERB_CHECKPOINT_FILENAME)
  checkpointer = reverb.checkpointers.DefaultCheckpointer(path=REVERB_CHECKPOINT_FILENAME)
  del server
  server = start_reverb_server(max_size, checkpointer)

def test_smoke():
  seed = 100
  max_episode_length = 500
  env_name = 'peg-insert-side'
  env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
  env.seeded_rand_vec = True
  policy = SawyerUniversalV2Policy(env_name=env_name)
  observation = env.reset()
  for i in range(max_episode_length):
    action = policy.get_action(observation)
    observation, r, done, info = env.step(action)
    print('-' * 80)
    print('\n'.join(describe_obs(env_name, observation)))
    print('-' * 80)


if __name__ == '__main__':
  clize.run(generate)
