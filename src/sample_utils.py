from typing import Tuple
from metaworld.envs.mujoco.env_dict import MT10_V2, MT50_V2
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE
import random
import numpy as np
import easy_process
from tqdm import tqdm
import difflib
from collections import defaultdict
import json
import copy

DEFAULT_SEED = random.randrange(1000)

STR_PROJ_CACHE = {}


def str_project(src, targets):
    cache_key = (src, tuple(targets))
    if cache_key in STR_PROJ_CACHE:
        return STR_PROJ_CACHE[cache_key]
    matches = sorted(
        targets,
        key=lambda tgt: difflib.SequenceMatcher(None, tgt, src).ratio(),
        reverse=True,
    )
    STR_PROJ_CACHE[cache_key] = matches
    return matches


MT10_ENV_NAMES = [e[:-3] for e in MT10_V2.keys()]
MT50_ENV_NAMES = [e[:-3] for e in MT50_V2.keys()]


def make_env(env_name, seed: int):
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f"{env_name}-v2-goal-observable"](seed)
    env.seeded_rand_vec = True
    env.max_episode_length = 500
    return env


def sample_policy_or_random(env, policy, random_policy_prob):
    assert env.seeded_rand_vec
    observation = env.reset()
    use_random = False
    yield {"observation": observation}
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
        yield {
            "observation": observation,
            "action": action,
            "reward": reward,
            "done": done,
            "success": info["success"],
        }
        observation = next_obs


def vec_collect_noisy_episodes(envs, policy, noise_scale, n_episodes):
    episodes = []
    while len(episodes) < n_episodes:
        episodes.extend(vec_sample_noisy_policy(envs, policy, noise_scale))
    return episodes


def vec_sample_noisy_policy(envs, policy, noise_scale):
    assert all(env.seeded_rand_vec for env in envs)
    observations = [env.reset() for env in envs]
    episodes = [[] for obs in observations]
    for _ in range(envs[0].max_episode_length):
        actions, agent_info = policy.get_actions(observations)
        for i, env in enumerate(envs):
            action_noisy = actions[i] + np.random.normal(
                scale=noise_scale, size=(actions[i].shape)
            )
            next_obs, reward, done, info = env.step(action_noisy)
            data = {
                "observation": observations[i],
                "action": actions[i],
                "action_noisy": action_noisy,
                "reward": reward,
                "done": done,
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


def sample_noisy_policy(env, policy, noise_scale):
    observation = env.reset()
    yield {"observation": observation}
    for i in range(env.max_episode_length):
        action, agent_info = policy.get_action(observation)
        action_noisy = action + np.random.normal(scale=noise_scale, size=action.shape)
        next_obs, reward, done, info = env.step(action_noisy)
        data = {
            "observation": observation,
            "action": action,
            "action_noisy": action_noisy,
            "reward": reward,
            "done": done,
        }
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
        data = {
            "observation": observation,
            "next_observation": next_obs,
            "action": action,
            "action_noisy": action_noisy,
            "reward": reward,
            "done": done,
        }
        for (k, v) in info.items():
            assert k not in data
            data[k] = v
        for (k, v) in agent_info.items():
            assert k not in data
            data[k] = v
        yield data
        observation = next_obs


@easy_process.subprocess_func
def noisy_sample_process(
    *, env_name: str, policy, noise_scale: float, seed: int, parent
):
    env = make_env(env_name, seed)

    while True:
        episode = []
        for data in sample_noisy_policy(env, policy, noise_scale):
            data["env_name"] = env_name
            episode.append(data)
        parent.sendrecv(episode)


def collect_noisy_episodes(
    env_names, policy, *, n_episodes=100, seed=100, noise_scale=0.1
):
    episodes = []
    with easy_process.Scope():
        workers = [
            noisy_sample_process(
                env_name=env_name, policy=policy, seed=seed, noise_scale=noise_scale
            )
            for env_name in env_names
        ]
        with tqdm(total=n_episodes) as pbar:
            while len(episodes) < n_episodes:
                for worker in workers:
                    episode = worker.recv(block=False)
                    if episode:
                        episodes.append(episode)
                        pbar.update(1)
    return episodes


def evaluate_policy(env_name, episodes) -> Tuple[float, float]:
    print("Evaluating", env_name)
    successes = []
    rewards = []
    controller_counts = defaultdict(int)
    candidate_counts = defaultdict(int)
    for episode in episodes:
        success = False
        episode_rewards = []
        for data in episode:
            success |= data.get("success", 0) > 0
            if "controller_name" in data:
                controller_counts[data["controller_name"]] += 1
            for candidate in data.get("candidate_controllers", []):
                candidate_counts[candidate] += 1
            if "reward" in data:
                episode_rewards.append(data["reward"])
        rewards.append(np.mean(episode_rewards))
        successes.append(success)
    print("Success rate for", env_name, ":", np.mean(successes))
    print("Avg timestep reward for", env_name, ":", np.mean(rewards))
    return np.mean(successes), np.mean(rewards)


def mean(seq):
    assert len(seq) > 0
    return np.mean(seq)


def episode_to_success(episode):
    success = False
    for data in episode:
        success |= data.get("success", 0) > 0
    return success


def average_reward(episode):
    return mean([data["reward"] for data in episode if "reward" in data])


class Evaluator:
    def __init__(
        self,
        seed,
        env_names,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
    ):
        self.envs = {env_name: make_env(env_name, seed) for env_name in env_names}
        self.noise_scale = noise_scale
        self.n_episodes = 50
        if base_infos is None:
            base_infos = {}
        self.base_infos = base_infos
        self.results_proc = results_proc
        self.output_filename = output_filename
        if output_filename:
            with open(output_filename, "w") as f:
                # Truncate the output file
                pass

    def evaluate(self, policy):
        infos = self.base_infos.copy()
        for (env_name, env) in self.envs.items():
            policy.env_name = env_name
            successes = []
            rewards = []
            with tqdm(total=self.n_episodes) as pbar:
                while len(successes) < self.n_episodes:
                    episode = list(sample_noisy_policy(env, policy, self.noise_scale))
                    successes.append(episode_to_success(episode))
                    rewards.append(average_reward(episode))
                    pbar.update(1)
            print(f"Success rate for {env_name}:", mean(successes))
            infos[f"{env_name}/SuccessRate"] = mean(successes)
            infos[f"{env_name}/RewardMean"] = mean(rewards)
        if self.output_filename:
            with open(self.output_filename, "a") as f:
                json.dump(infos, f)
                f.write("\n")
        return infos


def eval_policy(
    policy,
    env_name: str,
    *,
    seed,
    noise_scale: float = 0.0,
    n_episodes: int = 100,
    vec_envs: int = 1,
) -> Tuple[float, float]:
    envs = [make_env(env_name, seed + i) for i in range(vec_envs)]
    episodes = vec_collect_noisy_episodes(
        envs, policy, noise_scale, n_episodes=n_episodes
    )
    return evaluate_policy(policy, episodes)
