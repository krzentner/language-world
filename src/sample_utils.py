from metaworld.envs.mujoco.env_dict import MT10_V2
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE
import numpy as np

MT10_ENV_NAMES = [e[:-3] for e in MT10_V2.keys()]

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
        action, info = policy.get_action(observation)
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
      action, agent_info = policy.get_action(observation)
      action_noisy = action + np.random.normal(scale=noise_scale)
      next_obs, reward, done, info = env.step(action_noisy)
      data = {'observation': observation,
              'action': action,
              'action_noisy': action_noisy,
              'reward': reward,
              'done': done}
      for (k, v) in info.items():
        assert k not in data
        data[k] = v
      for (k, v) in agent_info.items():
        assert k not in data
        data[k] = v
      yield data
      observation = next_obs


def sample_policy_with_noise_process(env, policy, process):
  process.reset()
  observation = env.reset()
  yield {'observation': observation}
  for i in range(env.max_episode_length):
    action, agent_info = policy.get_action(observation)
    action_noisy = action + process.simulate()
    next_obs, reward, done, info = env.step(action_noisy)
    data = {'observation': observation,
            'action': action,
            'action_noisy': action_noisy,
            'reward': reward,
            'done': done}
    for (k, v) in info.items():
      assert k not in data
      data[k] = v
    for (k, v) in agent_info.items():
      assert k not in data
      data[k] = v
    yield data
    observation = next_obs
