import shutil as sh
from collections import defaultdict
from pprint import pprint
from dataclasses import dataclass
import random

import numpy as np
import clize
from tqdm import tqdm

from metaworld.envs.mujoco.env_dict import MT10_V2
import metaworld_controllers
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs, run_controller
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE

import ou_process

import reverb

REVERB_CHECKPOINT_FILENAME = 'data/reverb_checkpoint'

def describe_relative_coordinates(xyz1, xyz2):
  descriptors = {
      "near": 0,
      "left of": 0,
      "right of": 0,
      "behind": 0,
      "in front of": 0,
      "above": 0,
      "below": 0,
  }
  if np.linalg.norm(xyz1 - xyz2) < .04:
    descriptors["near"] = 1.
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

def describe_obs(env_name, obs):
  if not isinstance(obs, dict):
    obs = parse_obs(obs)
  keys_to_names = {'hand_pos': "the robot's gripper"}
  keys_to_names.update(OBJECT_NAMES[env_name])
  descriptors = {}
  for (key1, name1) in keys_to_names.items():
    for (key2, name2) in keys_to_names.items():
      if key1 == key2:
        continue
      disc = describe_relative_coordinates(obs[key1], obs[key2])
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
          action = policy.get_action(observation)
        observation, r, done, info = env.step(action)
      store_obs(client, observation)
  checkpoint_file = client.checkpoint()
  sh.copytree(checkpoint_file, REVERB_CHECKPOINT_FILENAME)
  print('Saving checkpoint to:', REVERB_CHECKPOINT_FILENAME)
  checkpointer = reverb.checkpointers.DefaultCheckpointer(path=REVERB_CHECKPOINT_FILENAME)
  del server
  server = start_reverb_server(max_size, checkpointer)

def make_env(env_name, seed: int):
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
    env.seeded_rand_vec = True
    env.max_episode_length = 500
    return env

def sample_policy_or_random(env, policy, random_policy_prob):
    observation = env.reset()
    use_random = False
    yield {'observation': observation}
    for i in range(env.max_episode_length):
      if i > 0 and not use_random and np.random.uniform() < random_policy_prob:
        use_random = True
      if use_random:
        noise = env.action_space.sample()
        alpha = 0.9
        action = alpha * action + (1 - alpha) * noise
      else:
        action = policy.get_action(observation)
      next_obs, reward, done, info = env.step(action)
      yield {'observation': observation,
             'action': action,
             'reward': reward,
             'done': done,
             'success': info['success']}
      observation = next_obs


def sample_noisy_policy(env, policy, noise_scale):
    observation = env.reset()
    yield {'observation': observation}
    for i in range(env.max_episode_length):
      action = policy.get_action(observation)
      action_noisy = action + np.random.normal(scale=noise_scale)
      next_obs, reward, done, info = env.step(action_noisy)
      yield {'observation': observation,
             'action': action,
             'action_noisy': action_noisy,
             'reward': reward,
             'done': done,
             'success': info['success']}
      observation = next_obs


def sample_policy_with_noise_process(env, policy, process):
  process.reset()
  observation = env.reset()
  yield {'observation': observation}
  for i in range(env.max_episode_length):
    action = policy.get_action(observation)
    action_noisy = action + process.simulate()
    next_obs, reward, done, info = env.step(action_noisy)
    yield {'observation': observation,
            'action': action,
            'action_noisy': action_noisy,
            'reward': reward,
            'done': done,
            'success': info['success']}
    observation = next_obs

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

  def get_action(self, observation):
    tree = metaworld_controllers.DECISION_TREES[self.env_name]['function']
    obs = parse_obs(observation)
    descriptions = describe_obs(self.env_name, obs)
    candidate_controllers = [
        con for (desc, con) in self.descriptor_to_controller.items()
        if descriptions[desc] > 0]
    if candidate_controllers:
      controller_name = random.choice(candidate_controllers)
    else:
      controller_name = random.choice(list(self.descriptor_to_controller.values()))
    ground_truth_controller_name = tree(obs)
    # if controller_name != ground_truth_controller_name:
      # print('candidate_controllers:', candidate_controllers)
      # print('ground_truth_controller:', ground_truth_controller_name)
      # pprint(descriptions)
    return run_controller(controller_name, obs)

def evaluate_policy(env_name, n_episodes, episode_factory):
  successes = []
  for i in tqdm(range(n_episodes)):
    success = False
    for data in episode_factory():
      success |= data.get('success', 0) > 0
    successes.append(success)
  print('Success rate for', env_name, ':', np.mean(successes))
  return np.mean(successes)


def find_controllers_with_missing_descriptors(seed=100):
  # For each descriptor, record how many observations with that descriptor each
  # controller is active
  # For each controller, look through each of these descriptor distributions,
  # and choose the best descriptor
  # Compose into policy, and count timesteps where policy disagrees with
  # original tree
  # for env_name in ['button-press-topdown']:
  for env_name in MT10_ENV_NAMES:
    desc_to_con_count = defaultdict(lambda: defaultdict(int))
    tree = metaworld_controllers.DECISION_TREES[env_name]['function']
    policy = SawyerUniversalV2Policy(env_name=env_name)
    env = make_env(env_name, seed)
    for episode in tqdm(range(10)):
      for data in sample_noisy_policy(env, policy, 0.01):
        obs = parse_obs(data['observation'])
        controller_name = tree(obs)
        descriptions = describe_obs(env_name, obs)
        for (desc, value) in descriptions.items():
          desc_to_con_count[desc][controller_name] += value
    policy_desc_to_con = {}
    for con_name in controller_names_for_env(env_name):
      best_descriptors = sorted(desc_to_con_count.items(),
                                key=lambda items:
                                2 * items[1][con_name] - sum(items[1].values()),
                                reverse=True)
      for (descriptor, counts) in best_descriptors:
        if descriptor not in policy_desc_to_con:
          print('Chose descriptor', repr(descriptor),
                'for controller', repr(con_name),
                '(matches for', counts[con_name], 'timesteps)')
          policy_desc_to_con[descriptor] = con_name
          break
    desc_policy = DescriptorPolicy(policy_desc_to_con, env_name=env_name)
    evaluate_policy(env_name, 10,
                    lambda: sample_noisy_policy(env, desc_policy, 0.01))


  # for env_name in MT10_ENV_NAMES:
    # controller_desc_counts = defaultdict(lambda: defaultdict(int))
    # controller_counts = defaultdict(int)
    # env_counts = defaultdict(int)
    # tree = metaworld_controllers.DECISION_TREES[env_name]['function']
    # successes = []
    # for episode in tqdm(range(10)):
      # success = False
      # for data in sample_noisy_policy(env, policy, 0.01):
        # o_d = parse_obs(data['observation'])
        # controller_name = tree(o_d)
        # update_counts(controller_desc_counts[controller_name],
                      # env_name, data['observation'])
        # update_counts(env_counts, env_name, data['observation'])
        # success |= data.get('success', 0) > 0
      # successes.append(success)
    # print('Success rate for', env_name, ':', np.mean(successes))
    # controller_desc_less_env = {
        # controller_name: {desc: (controller_desc_counts[controller_name][desc]
                                 # - env_count[desc])
                          # for desc in desc_counts.keys()}
      # for controller_name in controller_desc_counts.keys()
    # }
    # for (controller_name, counts) in controller_desc_less_env.items():
      # sorted_controllers =



def test_smoke():
  seed = 100
  env_name = 'peg-insert-side'
  env = make_env(env_name)
  policy = SawyerUniversalV2Policy(env_name=env_name)
  observation = env.reset()
  for i in range(env.max_episode_length):
    action = policy.get_action(observation)
    observation, r, done, info = env.step(action)
    print('-' * 80)
    print('\n'.join(describe_obs(env_name, observation)))
    print('-' * 80)


if __name__ == '__main__':
  clize.run(find_controllers_with_missing_descriptors)
