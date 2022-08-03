from metaworld.envs.mujoco.env_dict import MT10_V2, MT50_V2
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE
import numpy as np
import easy_process
from tqdm import tqdm

MT10_ENV_NAMES = [e[:-3] for e in MT10_V2.keys()]
MT50_ENV_NAMES = [e[:-3] for e in MT50_V2.keys()]

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
      action_noisy = action + np.random.normal(scale=noise_scale,
                                               size=action.shape)
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
  for i in range(env.max_episode_length):
    action, agent_info = policy.get_action(observation)
    action_noisy = action + process.simulate()
    next_obs, reward, done, info = env.step(action_noisy)
    data = {'observation': observation,
            'next_observation': next_obs,
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


@easy_process.subprocess_func
def noisy_sample_process(*, env_name: str, policy, noise_scale: float, seed: int, parent):
  env = make_env(env_name, seed)

  while True:
    episode = []
    for data in sample_noisy_policy(env, policy, noise_scale):
      data['env_name'] = env_name
      episode.append(data)
    parent.sendrecv(episode)


def collect_noisy_episodes(env_names, policy, *, n_episodes=100, seed=100,
                           noise_scale=0.1):
  episodes = []
  with easy_process.Scope():
    workers = [noisy_sample_process(env_name=env_name, policy=policy, seed=seed,
                                    noise_scale=noise_scale)
              for env_name in env_names]
    with tqdm(total=n_episodes) as pbar:
      while len(episodes) < n_episodes:
        for worker in workers:
          episode = worker.recv(block=False)
          if episode:
            episodes.append(episode)
            pbar.update(1)
  return episodes
