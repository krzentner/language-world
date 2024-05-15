import clize
import shutil as sh
from collections import defaultdict
from pprint import pprint
from dataclasses import dataclass
from functools import partial
import random
import os
import pickle

import numpy as np

import clize
from tqdm import tqdm

import easy_process
from metaworld.envs.mujoco.env_dict import MT10_V2
import metaworld_scripted_skills
from metaworld_scripted_skills import (
    SawyerUniversalV2Policy,
    parse_obs,
    run_scripted_skill,
)
import metaworld_universal_policy
from sample_utils import (
    make_env,
    sample_noisy_policy,
    sample_policy_with_noise_process,
    collect_noisy_episodes,
)
from run_utils import float_list, str_list
import sample_utils
from sample_utils import MT50_ENV_NAMES
import ou_process

from generate_metaworld_scene_dataset import describe_obs


def update_counts(descriptor_counts, env_name, observation):
    descriptions = describe_obs(env_name, observation)
    for (description, truth_value) in descriptions.items():
        if truth_value > 0:
            descriptor_counts[description] += 1


MT10_ENV_NAMES = [e[:-3] for e in MT10_V2.keys()]


def count_descriptors(
    n_episodes_per_env=100,
    random_policy_prob=0.01,
    envs=",".join(MT10_ENV_NAMES),
    seed=100,
):
    env_names = list(envs.split(","))
    descriptor_counts = defaultdict(int)
    for env_name in env_names:
        print("Gathering", env_name, "...")
        env = make_env(env_name, seed)
        policy = SawyerUniversalV2Policy(env_name=env_name)
        successes = []
        ou_proc = ou_process.OUProcess(dimensions=4)
        for episode in tqdm(range(n_episodes_per_env)):
            success = False
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                update_counts(descriptor_counts, env_name, data["observation"])
                success |= data.get("success", 0) > 0
            successes.append(success)
        print("Success rate for", env_name, ":", np.mean(successes))
    pprint(descriptor_counts)
    return descriptor_counts


def scripted_skill_names_for_env(env_name):
    for (
        scripted_skill_name,
        scripted_skill,
    ) in metaworld_scripted_skills.SCRIPTED_SKILLS.items():
        if scripted_skill["env-name"] == env_name:
            yield scripted_skill_name


@easy_process.subprocess_func
def sample_process(*, env_name: str, noise_scales: [float], seed: int, parent):
    env = make_env(env_name, seed)
    policy = metaworld_universal_policy.SawyerUniversalV2Policy(env_name=env_name)

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            ou_proc = OUProcess(dimensions=env.action_space.shape[0], sigma=noise_scale)
            episode = []
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                describe_obs(env_name, data["observation"])
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
            parent.sendrecv(episode)


def test_parallel(
    envs: str_list = MT50_ENV_NAMES,
    seed=sample_utils.DEFAULT_SEED,
    noise_scales: float_list = [0.1, 0.2, 0.5, 0.9],
):
    with easy_process.Scope():
        workers = [
            sample_process(env_name=env_name, seed=seed, noise_scales=noise_scales)
            for env_name in envs
        ]
        datapoints = []
        with tqdm(total=len(envs) * len(noise_scales)) as pbar:
            for _ in range(len(noise_scales)):
                for worker in workers:
                    episode = worker.recv(block=True)
                    datapoints.extend(episode)
                    pbar.update(1)


@dataclass
class DescriptorPolicy:
    descriptor_to_scripted_skill: dict
    env_name: str
    scripted_skill_choice_prob: float = 1.0
    base_weight: float or None = None

    def get_action(self, observation):
        tree = metaworld_scripted_skills.DECISION_TREES[self.env_name]["function"]
        obs = parse_obs(observation)
        descriptions = describe_obs(self.env_name, obs)
        candidate_scripted_skills = [
            con
            for (desc, con) in self.descriptor_to_scripted_skill.items()
            if descriptions[desc] > 0
        ]
        if (
            candidate_scripted_skills
            and np.random.uniform() < self.scripted_skill_choice_prob
        ):
            scripted_skill_name = random.choice(candidate_scripted_skills)
        else:
            scripted_skill_name = random.choice(
                list(self.descriptor_to_scripted_skill.values())
            )
        ground_truth_scripted_skill_name = tree(obs)
        info = {}
        info["scripted_skill_name"] = scripted_skill_name
        info["candidate_scripted_skills"] = list(set(candidate_scripted_skills))
        if self.base_weight:
            descriptors = list(self.descriptor_to_scripted_skill.keys())
            weights = np.array(
                [
                    1.0 if descriptions[desc] > 0 else self.base_weight
                    for desc in descriptors
                ]
            )
            weights /= weights.sum()
            actions = np.array(
                [
                    run_scripted_skill(self.descriptor_to_scripted_skill[desc], obs)
                    for desc in descriptors
                ]
            )
            weighted_action = np.einsum("i,ik->k", weights, actions)
            return weighted_action, info
        else:
            return run_scripted_skill(scripted_skill_name, obs), info


def evaluate_policy(env_name, episodes):
    print("Evaluating", env_name)
    successes = []
    scripted_skill_counts = defaultdict(int)
    candidate_counts = defaultdict(int)
    for episode in episodes:
        success = False
        for data in episode:
            success |= data.get("success", 0) > 0
            if "scripted_skill_name" in data:
                scripted_skill_counts[data["scripted_skill_name"]] += 1
            for candidate in data.get("candidate_scripted_skills", []):
                candidate_counts[candidate] += 1
        successes.append(success)
    print("Success rate for", env_name, ":", np.mean(successes))
    print("scripted_skill_counts:")
    pprint(dict(scripted_skill_counts))
    print("candidate_counts:")
    pprint(dict(candidate_counts))
    return np.mean(successes)


def find_most_likely_plans(
    *,
    envs=",".join(MT10_ENV_NAMES),
    seed=100,
    scripted_skill_map_filename=os.path.expanduser("~/data/scripted_skill_map.pkl")
):
    env_names = list(envs.split(","))
    # For each descriptor, record how many observations with that descriptor each
    # scripted_skill is active
    # For each scripted_skill, look through each of these descriptor distributions,
    # and choose the best descriptor
    # Compose into policy, and count timesteps where policy disagrees with
    # original tree
    # for env_name in ['button-press-topdown']:
    success_rates = {}
    scripted_skill_maps = {}
    for env_name in env_names:
        desc_to_con_count = defaultdict(lambda: defaultdict(int))
        tree = metaworld_scripted_skills.DECISION_TREES[env_name]["function"]
        policy = SawyerUniversalV2Policy(env_name=env_name)
        env = make_env(env_name, seed)
        scripted_skill_total_counts = defaultdict(int)
        episodes = collect_noisy_episodes(
            10 * [env_name], policy, n_episodes=100, seed=seed, noise_scale=0.1
        )
        # for episode in tqdm(range(100)):
        # ou_proc = ou_process.OUProcess(dimensions=4)
        # for data in sample_noisy_policy(env, policy, 0.01):
        for episode in tqdm(episodes):
            for data in episode:
                # for data in sample_policy_with_noise_process(env, policy, ou_proc):
                obs = parse_obs(data["observation"])
                scripted_skill_name = tree(obs)
                descriptions = describe_obs(env_name, obs)
                for (desc, value) in descriptions.items():
                    desc_to_con_count[desc][scripted_skill_name] += value
                scripted_skill_total_counts[scripted_skill_name] += 1
        policy_desc_to_con = {}
        for con_name in scripted_skill_names_for_env(env_name):
            # Maximize number of timesteps where the description is present for this
            # scripted_skill and no other scripted_skills.
            best_descriptors = sorted(
                desc_to_con_count.items(),
                key=lambda items: (
                    items[1][con_name] - (sum(items[1].values()) - items[1][con_name])
                ),
                reverse=True,
            )
            num_chosen = 0
            for (descriptor, counts) in best_descriptors:
                print(
                    "Chose descriptor",
                    repr(descriptor),
                    "for scripted_skill",
                    repr(con_name),
                    "(matches for",
                    counts[con_name],
                    "/",
                    scripted_skill_total_counts[con_name],
                    "timesteps)",
                )
                policy_desc_to_con[descriptor] = con_name
                num_chosen += 1
                if num_chosen >= 1:
                    break
        print(policy_desc_to_con)
        scripted_skill_maps[env_name] = policy_desc_to_con
        desc_policy = DescriptorPolicy(policy_desc_to_con, env_name=env_name)
        scripted_skill_prob = 0.1
        print("Weighting incorrect scripted_skill by", scripted_skill_prob)
        desc_policy.base_weight = scripted_skill_prob
        success = evaluate_policy(
            env_name,
            collect_noisy_episodes(
                20 * [env_name], desc_policy, seed=seed, n_episodes=100, noise_scale=0.1
            ),
        )
        desc_policy.base_weight = None
        success = evaluate_policy(
            env_name,
            collect_noisy_episodes(
                20 * [env_name], desc_policy, seed=seed, n_episodes=100, noise_scale=0.1
            ),
        )
        success_rates[env_name] = success
    print(success_rates)
    print(scripted_skill_maps)
    with open(scripted_skill_map_filename, "wb") as f:
        pickle.dump(scripted_skill_maps, f)


def run(output):
    find_most_likely_plans(scripted_skill_map_filename=output)


if __name__ == "__main__":
    clize.run(run)