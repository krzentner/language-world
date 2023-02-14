import collections

import numpy as np


class Policy:
    def get_action(self, state: "state", prev_info: dict) -> tuple["action", dict]:
        pass


class Env:
    def step(self, action) -> tuple["obs", float, bool, dict]:
        pass


class InProgressEpisode:
    """An in-progress episode.

    Args:
        env (Environment): The environment the trajectory is being collected
            in.
        initial_observation (np.ndarray): The first observation. If None, the
            environment will be reset to generate this observation.
        episode_info (dict[str, np.ndarray]): Info for this episode.

    Raises:
        ValueError: if either initial_observation and episode_info is passed in
            but not the other. Either both or neither should be passed in.

    """

    def __init__(self, env, initial_observation=None, episode_id=None):
        if initial_observation is None:
            initial_observation = env.reset()
        self.episode_id = episode_id
        self.env = env
        self.observations = [initial_observation]
        self.actions = []
        self.rewards = []
        self.dones = []
        self.agent_infos = collections.defaultdict(list)
        self.env_infos = collections.defaultdict(list)
        self.n_steps = 0

    def step(self, action, agent_info):
        """Step the episode using an action from an agent.

        Args:
            action (np.ndarray): The action taken by the agent.
            agent_info (dict[str, np.ndarray]): Extra agent information.

        Returns:
            np.ndarray: The new observation from the environment.

        """
        next_obs, reward, dones, env_info = self.env.step(action)

        self.observations.append(next_obs)
        self.rewards.append(reward)
        self.actions.append(action)
        for k, v in agent_info.items():
            self.agent_infos[k].append(v)
        for k, v in env_info.items():
            self.env_infos[k].append(v)
        self.dones.append(dones)
        self.n_steps += 1
        return next_obs

    @property
    def last_obs(self):
        """np.ndarray: The last observation in the epside."""
        return self.observations[-1]

    def drain(self) -> dict[str, list]:
        data = {
            "observation": self.observations[:-1],
            "action": self.actions,
            "rewards": self.rewards,
            "dones": self.dones,
        }
        for k, v in self.agent_infos.items():
            data[f"agent_info-{k}"] = v
        for k, v in self.env_infos.items():
            data[f"agent_info-{k}"] = v

        self.observations = [self.observations[-1]]
        self.actions = []
        self.rewards = []
        self.dones = []
        self.agent_infos = collections.defaultdict(list)
        self.env_infos = collections.defaultdict(list)
        return data


class VecSampler:
    def __init__(self, policy, envs, episode_id_start):
        self._envs = envs
        self.policy = policy
        self._next_episode_id = episode_id_start
        episodes = []
        for env in self._envs:
            episode_id = self._next_episode_id
            self._next_episode_id += 1
            initial_obs = env.reset()
            episodes.append(InProgressEpisode(env, env, initial_obs, episode_id))
        self._in_progress_episodes = episodes
        self._completed_episodes = {}

    def collect(self, n_timesteps):
        n_vec_steps = int(n_timesteps // self._envs)
        assert n_timesteps % self._envs == 0
        for _ in range(n_vec_steps):
            observations = [ep.last_obs for ep in self._in_progress_episodes]
            actions, agent_info = self.policy.get_actions(observations)
            for i, action in enumerate(actions):
                self._in_progress_episodes[i].step(
                    action, {k: v[i] for k, v in agent_info.items()}
                )


def vec_sampl(envs, policy, noise_scale):
    assert all(env.seeded_rand_vec for env in envs)
    observations = [env.reset() for env in envs]
    episodes = [[] for obs in observations]
    for _ in range(envs[0].max_episode_length):
        actions, agent_info = policy.get_actions(observations)
        for i, env in enumerate(envs):
            action_noisy = actions[i] + np.random.normal(
                scale=noise_scale, size=(actions[i].shape)
            )
            next_obs, reward, dones, info = env.step(action_noisy)
            data = {
                "observation": observations[i],
                "action": actions[i],
                "action_noisy": action_noisy,
                "reward": reward,
                "dones": dones,
            }
            for (k, v) in info.items():
                assert k not in data
                data[k] = v
            for (k, v) in agent_info.items():
                assert k not in data
                data[k] = v[i]
            episodes[i].append(data)
            observations[i] = next_obs
    return episodes
