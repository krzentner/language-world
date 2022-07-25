import shutil as sh
from collections import defaultdict
from pprint import pprint
from dataclasses import dataclass
import random
import os
import pickle

import numpy as np
import clize
from tqdm import tqdm

from metaworld.envs.mujoco.env_dict import MT10_V2
import metaworld_controllers
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs, run_controller
from sample_utils import (make_env, sample_noisy_policy,
                          sample_policy_with_noise_process, collect_noisy_episodes)
from sample_utils import MT50_ENV_NAMES

import ou_process

import reverb

REVERB_CHECKPOINT_FILENAME = 'data/reverb_checkpoint'

class FixedDict(dict):

  def __setitem__(self, key, value):
    assert key in self, f"{key} not present in dict"
    return super().__setitem__(key, value)

def describe_symmetric_coordinates(xyz1, xyz2):
  descriptors = FixedDict({
      "near": 0,
      "around": 0,
      "left of": 0,
      "right of": 0,
      "behind": 0,
      "in front of": 0,
      "above": 0,
      "below": 0,
      "vertically aligned with": 0,
      "almost vertically aligned with": 0,
      "mostly below": 0,
      "horizontally aligned with": 0,
      "forward aligned with": 0,
  })
  if np.linalg.norm(xyz1 - xyz2) < .04:
    descriptors["near"] = 1.
  if np.linalg.norm(xyz1 - xyz2 + [0, 0, 0.02]) < .03:
    descriptors["around"] = 1.
  if xyz1[0] - xyz2[0] > 0.04:
    descriptors["left of"] = 1.
  if xyz1[0] - xyz2[0] < -0.04:
    descriptors["right of"] = 1.
  if (xyz1[1] - xyz2[1] > 0.04 and np.linalg.norm(xyz1[[0,2]] - xyz2[[0, 2]]) < 0.04):
    descriptors["behind"] = 1.
  if (xyz1[1] - xyz2[1] < -0.04 and np.linalg.norm(xyz1[[0,2]] - xyz2[[0, 2]]) < 0.04):
    descriptors["in front of"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] > 0.:
    descriptors["above"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] < 0:
    descriptors["below"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.06:
    descriptors["vertically aligned with"] = 1.
  if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.12:
    descriptors["almost vertically aligned with"] = 1.
  if xyz1[2] < xyz2[2] + 0.23:
    descriptors["mostly below"] = 1.
  if np.linalg.norm(xyz1[1:] - xyz2[1:]) < 0.03:
    descriptors["horizontally aligned with"] = 1.
  if np.linalg.norm(xyz1[[0,2]] - xyz2[[0,2]]) < 0.03:
    descriptors["forward aligned with"] = 1.
  descriptors = dict(descriptors)
  for key in list(descriptors.keys()):
    descriptors[f"not {key}"] = 1 - descriptors[key]
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
        # The goal is weirdly offset, so it's hacked in below
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
    },
    'sweep': {
        'obj1_pos': "cube",
        'goal_pos': "target location",
    },
    'assembly': {
        'obj1_pos': "wrench",
        'goal_pos': "peg",
    },
    'basketball': {
        'obj1_pos': "ball",
        'goal_pos': "hoop",
    },
    'bin-picking': {
        'obj1_pos': "cube",
    },
    'box-close': {
        'obj1_pos': "lid",
        'goal_pos': "box",
    },
    'button-press-topdown-wall': {
        'obj1_pos': "button",
    },
    'button-press': {
        'obj1_pos': "button",
    },
    'button-press-wall': {
        'obj1_pos': "button",
    },
    'coffee-button': {
        'obj1_pos': "button",
    },
    'coffee-pull': {
        'obj1_pos': "mug",
    },
    'coffee-push': {
        'obj1_pos': "mug",
        'goal_pos': "target location",
    },
    'dial-turn': {
        'obj1_pos': "dial",
    },
    'disassemble': {
        'obj1_pos': "wrench",
        'goal_pos': "peg",
    },
    'door-close': {
        'obj1_pos': "door",
        'goal_pos': "target location",
    },
    'door-lock': {
        'obj1_pos': "door's lock",
    },
    'door-unlock': {
        'obj1_pos': "door's lock",
    },
    'faucet-close': {
        'obj1_pos': "faucet",
    },
    'faucet-open': {
        'obj1_pos': "faucet",
    },
    'hammer': {
        'obj1_pos': "hammer",
    },
    'hand-insert': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'handle-press-side': {
        'obj1_pos': "handle",
    },
    'handle-press': {
        'obj1_pos': "handle",
    },
    'handle-pull-side': {
        'obj1_pos': "handle",
    },
    'handle-pull': {
        'obj1_pos': "handle",
    },
    'lever-pull': {
        'obj1_pos': "lever",
    },
    'peg-unplug-side': {
        'obj1_pos': "peg",
    },
    'pick-out-of-hole': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'pick-place-wall': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'plate-slide-back-side': {
        'obj1_pos': "plate",
    },
    'plate-slide-back': {
        'obj1_pos': "plate",
    },
    'plate-slide-side': {
        'obj1_pos': "plate",
    },
    'plate-slide': {
        'obj1_pos': "plate",
        'goal_pos': "target location",
    },
    'push-back': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'push-wall': {
        'obj1_pos': "puck",
        'goal_pos': "target location",
    },
    'reach-wall': {
        'goal_pos': "target location",
    },
    'shelf-place': {
        'obj1_pos': "block",
        'goal_pos': "shelf",
    },
    'soccer': {
        'obj1_pos': "ball",
        'goal_pos': "goal",
    },
    'stick-pull': {
        'obj1_pos': "stick",
        'obj2_pos': "thermos",
        'goal_pos': "target location",
    },
    'stick-push': {
        'obj1_pos': "stick",
        'obj2_pos': "thermos",
        'goal_pos': "target location",
    },
    'sweep-into': {
        'obj1_pos': "cube",
        'goal_pos': "target location",
    },
    'sweep': {
        'obj1_pos': "cube",
        'goal_pos': "target location",
    },
}

assert len(OBJECT_NAMES) == 50
assert set(OBJECT_NAMES.keys()) == set(MT50_ENV_NAMES)

def describe_obs(env_name, obs):
  if not isinstance(obs, dict):
    obs = parse_obs(obs)
  keys_to_names = {'hand_pos': "the robot's gripper"}
  keys_to_names.update(OBJECT_NAMES[env_name])
  descriptors = {}
  object_locations = []
  for (key, name) in OBJECT_NAMES[env_name].items():
    object_locations.append((name, obs[key]))
  object_locations.append(("the robot's gripper", obs['hand_pos']))
  if env_name == 'peg-insert-side':
    object_locations.append(("hole", np.array([-.35, obs['goal_pos'][1], .16])))
  for (i, (name1, xyz1)) in enumerate(object_locations):
    for (j, (name2, xyz2)) in enumerate(object_locations):
      if name1 == name2:
        continue
      # This runs (2-4x) faster, but is less complete
      # if i > j:
        # continue
      disc = describe_symmetric_coordinates(xyz1, xyz2)
      for (key, val) in disc.items():
        if key == 'around' or key == 'not around' and name1 != "the robot's gripper":
          continue
        descriptors[f"{name1} is {key} {name2}"] = val
  for (key, name) in OBJECT_NAMES[env_name].items():
    if key == 'goal_pos':
      continue
    gripper_motion = obs['hand_pos'] - obs['last_hand_pos']
    obj_motion = obs[key] - obs[f'last_{key}']

    if obs[key][2] > 0.02:
      descriptors[f"{name} is touching the table"] = 0.
      descriptors[f"{name} is not touching the table"] = 1.
    else:
      descriptors[f"{name} is touching the table"] = 1.
      descriptors[f"{name} is not touching the table"] = 0.

  if obs['gripper_distance_apart'] > 0.75:
    descriptors["gripper is open"] = 1.
    descriptors["gripper is closed"] = 0.
  else:
    descriptors["gripper is open"] = 0.
    descriptors["gripper is closed"] = 1.

  # for (key, value) in descriptors.items():
    # if value > 0:
      # print(key)
  conjunction_descriptors = {}
  for (desc1, value1) in descriptors.items():
    for (desc2, value2) in descriptors.items():
      conjunction_descriptors[f"{desc1} and {desc2}"] = value1 * value2
  descriptors.update(conjunction_descriptors)
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

def update_counts(descriptor_counts, env_name, observation):
  descriptions = describe_obs(env_name, observation)
  for (description, truth_value) in descriptions.items():
    if truth_value > 0:
      descriptor_counts[description] += 1


def generate(n_episodes_per_env=100, random_policy_prob=0.005,
             envs=','.join([e[:-3] for e in MT10_V2.keys()]), seed=100):
  env_names = list(envs.split(','))
  max_size = len(env_names) * n_episodes_per_env * 500
  server = start_reverb_server(max_size=max_size)
  client = reverb.Client(f'localhost:{server.port}')

  for env_name in env_names:
    print('Gathering', env_name, '...')
    env = make_env(env_name)
    policy = SawyerUniversalV2Policy(env_name=env_name)
    for episode in tqdm(range(n_episodes_per_env)):
      observation = env.reset()
      use_random = False
      for i in range(env.max_episode_length):
        store_obs(client, observation)
        if i > 0 and not use_random and np.random.uniform() < random_policy_prob:
          # print('switched to random on step', i)
          use_random = True
        if use_random:
          noise = env.action_space.sample()
          alpha = 0.9
          action = alpha * action + (1 - alpha) * noise
        else:
          action, info = policy.get_action(observation)
        observation, r, done, info = env.step(action)
      store_obs(client, observation)
  checkpoint_file = client.checkpoint()
  sh.copytree(checkpoint_file, REVERB_CHECKPOINT_FILENAME)
  print('Saving checkpoint to:', REVERB_CHECKPOINT_FILENAME)
  checkpointer = reverb.checkpointers.DefaultCheckpointer(path=REVERB_CHECKPOINT_FILENAME)
  del server
  server = start_reverb_server(max_size, checkpointer)

MT10_ENV_NAMES = [e[:-3] for e in MT10_V2.keys()]

def count_descriptors(n_episodes_per_env=100, random_policy_prob=0.01,
                      envs=','.join(MT10_ENV_NAMES), seed=100):
  env_names = list(envs.split(','))
  descriptor_counts = defaultdict(int)
  for env_name in env_names:
    print('Gathering', env_name, '...')
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)
    successes = []
    ou_proc = ou_process.OUProcess(dimensions=4)
    for episode in tqdm(range(n_episodes_per_env)):
      success = False
      for data in sample_policy_with_noise_process(env, policy, ou_proc):
        update_counts(descriptor_counts, env_name, data['observation'])
        success |= data.get('success', 0) > 0
      successes.append(success)
    print('Success rate for', env_name, ':', np.mean(successes))
  pprint(descriptor_counts)
  return descriptor_counts

def controller_names_for_env(env_name):
  for (controller_name, controller) in metaworld_controllers.CONTROLLERS.items():
    if controller['env-name'] == env_name:
      yield controller_name

@dataclass
class DescriptorPolicy:
  descriptor_to_controller: dict
  env_name: str
  controller_choice_prob: float = 1.0
  base_weight: float or None = None

  def get_action(self, observation):
    tree = metaworld_controllers.DECISION_TREES[self.env_name]['function']
    obs = parse_obs(observation)
    descriptions = describe_obs(self.env_name, obs)
    candidate_controllers = [
        con for (desc, con) in self.descriptor_to_controller.items()
        if descriptions[desc] > 0]
    if candidate_controllers and np.random.uniform() < self.controller_choice_prob:
      controller_name = random.choice(candidate_controllers)
    else:
      controller_name = random.choice(list(self.descriptor_to_controller.values()))
    ground_truth_controller_name = tree(obs)
    info = {}
    info['controller_name'] = controller_name
    info['candidate_controllers'] = list(set(candidate_controllers))
    if self.base_weight:
      descriptors = list(self.descriptor_to_controller.keys())
      weights = np.array([1. if descriptions[desc] > 0 else self.base_weight
                          for desc in descriptors])
      weights /= weights.sum()
      actions = np.array([run_controller(self.descriptor_to_controller[desc], obs)
                          for desc in descriptors])
      weighted_action = np.einsum('i,ik->k', weights, actions)
      return weighted_action, info
    else:
      return run_controller(controller_name, obs), info

def evaluate_policy(env_name, episodes):
  successes = []
  controller_counts = defaultdict(int)
  candidate_counts = defaultdict(int)
  for episode in episodes:
    success = False
    for data in episode:
      success |= data.get('success', 0) > 0
      if 'controller_name' in data:
        controller_counts[data['controller_name']] += 1
      for candidate in data.get('candidate_controllers', []):
        candidate_counts[candidate] += 1
    successes.append(success)
  print('Success rate for', env_name, ':', np.mean(successes))
  print('controller_counts:')
  pprint(dict(controller_counts))
  print('candidate_counts:')
  pprint(dict(candidate_counts))
  return np.mean(successes)


def find_controllers_with_missing_descriptors(*, envs=','.join(MT10_ENV_NAMES), seed=100):
  env_names = list(envs.split(','))
  # For each descriptor, record how many observations with that descriptor each
  # controller is active
  # For each controller, look through each of these descriptor distributions,
  # and choose the best descriptor
  # Compose into policy, and count timesteps where policy disagrees with
  # original tree
  # for env_name in ['button-press-topdown']:
  success_rates = {}
  controller_maps = {}
  for env_name in env_names:
    desc_to_con_count = defaultdict(lambda: defaultdict(int))
    tree = metaworld_controllers.DECISION_TREES[env_name]['function']
    policy = SawyerUniversalV2Policy(env_name=env_name)
    env = make_env(env_name, seed)
    controller_total_counts = defaultdict(int)
    episodes = collect_noisy_episodes(10 * [env_name],
                                      policy, n_episodes=100,
                                      seed=seed, noise_scale=0.1)
    # for episode in tqdm(range(100)):
      # ou_proc = ou_process.OUProcess(dimensions=4)
      # for data in sample_noisy_policy(env, policy, 0.01):
    for episode in tqdm(episodes):
      for data in episode:
      # for data in sample_policy_with_noise_process(env, policy, ou_proc):
        obs = parse_obs(data['observation'])
        controller_name = tree(obs)
        descriptions = describe_obs(env_name, obs)
        for (desc, value) in descriptions.items():
          desc_to_con_count[desc][controller_name] += value
        controller_total_counts[controller_name] += 1
    policy_desc_to_con = {}
    for con_name in controller_names_for_env(env_name):
      # Maximize number of timesteps where the description is present for this
      # controller and no other controllers.
      best_descriptors = sorted(desc_to_con_count.items(),
                                key=lambda items:
                                (items[1][con_name] -
                                 (sum(items[1].values()) - items[1][con_name])),
                                reverse=True)
      num_chosen = 0
      for (descriptor, counts) in best_descriptors:
        print('Chose descriptor', repr(descriptor),
              'for controller', repr(con_name),
              '(matches for', counts[con_name], '/',
              controller_total_counts[con_name], 'timesteps)')
        policy_desc_to_con[descriptor] = con_name
        num_chosen += 1
        if num_chosen >= 1:
          break
    print(policy_desc_to_con)
    controller_maps[env_name] = policy_desc_to_con
    desc_policy = DescriptorPolicy(policy_desc_to_con, env_name=env_name)
    controller_prob = 0.1
    print('Weighting incorrect controller by', controller_prob)
    desc_policy.base_weight = controller_prob
    success = evaluate_policy(env_name,
                              collect_noisy_episodes(20 * [env_name],
                                                     desc_policy,
                                                     seed=seed,
                                                     n_episodes=100,
                                                     noise_scale=0.1))
    # for controller_prob in np.linspace(0, 1, 11):
      # print('Weighting incorrect controller by', controller_prob)
      # desc_policy.base_weight = controller_prob
      # success = evaluate_policy(env_name, 10,
                                # lambda: sample_noisy_policy(env, desc_policy, 0.10))
      # desc_policy.base_weight = None
      # print('Using correct controller with prob', controller_prob)
      # desc_policy.controller_choice_prob = controller_prob
      # success = evaluate_policy(env_name, 10,
                                # lambda: sample_noisy_policy(env, desc_policy, 0.10))
      # if controller_prob == 1.0:
        # success_rates[env_name] = success
  print(success_rates)
  print(controller_maps)
  with open(os.path.expanduser('~/data/controller_map.pkl'), 'wb') as f:
    pickle.dump(controller_maps, f)


def test_smoke():
  seed = 100
  env_name = 'peg-insert-side'
  env = make_env(env_name, seed)
  policy = SawyerUniversalV2Policy(env_name=env_name)
  observation = env.reset()
  for i in range(env.max_episode_length):
    action, _ = policy.get_action(observation)
    observation, r, done, info = env.step(action)
    print('-' * 80)
    for (desc, truth_value) in describe_obs(env_name, observation).items():
      print(f"{desc}:", bool(truth_value))
    print('-' * 80)


if __name__ == '__main__':
  clize.run(find_controllers_with_missing_descriptors)
