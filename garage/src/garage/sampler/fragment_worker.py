"""Worker that "vectorizes" environments."""
import copy

from garage import EpisodeBatch, StepType
from garage.sampler import _apply_env_update, InProgressEpisode
from garage.sampler.default_worker import DefaultWorker


class FragmentWorker(DefaultWorker):
    """Vectorized Worker that collects partial episodes.

    Useful for off-policy RL.

    Args:
        seed (int): The seed to use to intialize random number generators.
        max_episode_length (int or float): The maximum length of episodes which
            will be sampled. Can be (floating point) infinity.
        length of fragments before they're transmitted out of
        worker_number (int): The number of the worker this update is
            occurring in. This argument is used to set a different seed for
            each worker.
        n_envs (int): Number of environment copies to use.
        min_fragment_length (int or None): Minimum fragment length to collect.
            Shorter fragments with terminal states may still be collected.
            None causes only full episodes to be collected.
        min_fragments_per_call (int): Minimum number of fragments to collect in
            a single rollout() call.

    """

    DEFAULT_N_ENVS = 8

    def __init__(
        self,
        *,
        seed,
        max_episode_length,
        worker_number,
        n_envs=DEFAULT_N_ENVS,
        min_fragment_length=1,
        min_fragments_per_call=1,
    ):
        super().__init__(
            seed=seed,
            max_episode_length=max_episode_length,
            worker_number=worker_number,
        )
        self._min_fragment_length = min_fragment_length
        self._min_fragments_per_call = min_fragments_per_call
        self._n_envs = n_envs
        self._needs_env_reset = True
        self._envs = [None] * n_envs
        self._episode_lengths = [0] * self._n_envs
        self._complete_fragments = []
        # Initialized in start_episode
        self._fragments = []
        self._next_episode_id = 0

    def _allocate_episode_id(self):
        episode_id = self._next_episode_id
        self._next_episode_id += 1
        return (self._worker_number, episode_id)

    def update_env(self, env_update):
        """Update the environments.

        If passed a list (*inside* this list passed to the Sampler itself),
        distributes the environments across the "vectorization" dimension.

        Args:
            env_update(Environment or EnvUpdate or None): The environment to
                replace the existing env with. Note that other implementations
                of `Worker` may take different types for this parameter.

        Raises:
            TypeError: If env_update is not one of the documented types.
            ValueError: If the wrong number of updates is passed.

        """
        if isinstance(env_update, list):
            if len(env_update) != self._n_envs:
                raise ValueError(
                    "If separate environments are passed for "
                    "each worker, there must be exactly n_envs "
                    "({}) environments, but received {} "
                    "environments.".format(self._n_envs, len(env_update))
                )
        elif env_update is not None:
            env_update = [copy.deepcopy(env_update) for _ in range(self._n_envs)]
        if env_update:
            for env_index, env_up in enumerate(env_update):
                self._envs[env_index], up = _apply_env_update(
                    self._envs[env_index], env_up
                )
                self._needs_env_reset |= up

    def start_episode(self):
        """Resets all agents if the environment was updated."""
        if self._needs_env_reset:
            self._needs_env_reset = False
            self.agent.reset([True] * len(self._envs))
            self._episode_lengths = [0] * len(self._envs)
            self._fragments = [
                InProgressEpisode(env, episode_id=self._allocate_episode_id())
                for env in self._envs
            ]

    def step_episode(self):
        """Take a single time-step in the current episode.

        Returns:
            bool: True iff at least one of the episodes was completed.

        """
        prev_obs = [frag.last_obs for frag in self._fragments]
        actions, agent_infos = self.agent.get_actions(prev_obs)
        completes = [False] * len(self._envs)
        for i, action in enumerate(actions):
            frag = self._fragments[i]
            if self._episode_lengths[i] < self._max_episode_length:
                agent_info = {k: v[i] for (k, v) in agent_infos.items()}
                frag.step(action, agent_info)
                self._episode_lengths[i] += 1
            if (
                self._episode_lengths[i] >= self._max_episode_length
                or frag.step_types[-1] == StepType.TERMINAL
            ):
                self._episode_lengths[i] = 0
                complete_frag = frag.to_batch()
                self._complete_fragments.append(complete_frag)
                self._fragments[i] = InProgressEpisode(
                    self._envs[i], episode_id=self._allocate_episode_id()
                )
                completes[i] = True
        if any(completes):
            self.agent.reset(completes)
        return any(completes)

    def collect_episode(self):
        """Gather fragments from all in-progress episodes.

        Returns:
            EpisodeBatch: A batch of the episode fragments.

        """
        for i, frag in enumerate(self._fragments):
            assert frag.env is self._envs[i]
            if (
                self._min_fragment_length
                and len(frag.rewards) >= self._min_fragment_length
            ):
                complete_frag = frag.to_batch()
                self._complete_fragments.append(complete_frag)
                self._fragments[i] = InProgressEpisode(
                    frag.env,
                    frag.last_obs,
                    frag.episode_info,
                    episode_id=frag.episode_id,
                )

    def rollout(self):
        """Sample a single episode of the agent in the environment.

        Returns:
            EpisodeBatch: The collected episode.

        """
        self.start_episode()
        while len(self._complete_fragments) < self._min_fragments_per_call:
            self.step_episode()
            self.collect_episode()
        assert len(self._complete_fragments) > 0
        result = EpisodeBatch.concatenate(*self._complete_fragments)
        self._complete_fragments = []
        return result

    def shutdown(self):
        """Close the worker's environments."""
        for env in self._envs:
            env.close()
