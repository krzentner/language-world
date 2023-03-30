import clize
from collections import defaultdict
from generate_metaworld_scene_dataset import (
    enumerate_base_conds,
    eval_conditions,
    parse_obs,
    enumerate_descriptors,
)
from metaworld_controllers import parse_obs
from metaworld_universal_policy import SawyerUniversalV2Policy
from run_utils import str_list
from generate_mt10_plans import load_and_parse_plans, plan_str
from tqdm import tqdm
import sample_utils
from pprint import pprint


def split_conds(env_name, obs, conditions, fuzzy):
    truth_values = eval_conditions(env_name, conditions, obs, fuzzy=fuzzy)
    true_conds = []
    false_conds = []
    for (cond, truth_value) in zip(conditions, truth_values):
        if truth_value:
            true_conds.append(cond)
        else:
            false_conds.append(cond)
    return true_conds, false_conds


def record_changes(counts, before, after):
    for cond in after:
        if cond not in before:
            counts[cond] += 1


def change_counts(env_name, episode, key_conditions, candidate_conds):
    before_conds = {}
    conditions_to_change_count = defaultdict(lambda: defaultdict(int))
    for (i, data) in enumerate(episode):
        obs = parse_obs(data["observation"])
        conds_now, _ = split_conds(env_name, obs, candidate_conds, fuzzy=False)
        true_keys, false_keys = split_conds(env_name, obs, key_conditions, fuzzy=False)
        if i + 1 == len(episode):
            # This is the last timestep
            # Record all of the changes
            for (key, before) in before_conds.items():
                record_changes(conditions_to_change_count[key], before, conds_now)
        else:
            # Record all of the conditions that were true when key started being
            # true
            for key in true_keys:
                if key not in before_conds:
                    before_conds[key] = conds_now
            # Record all of the conditions that became true while key was true
            for key in false_keys:
                if key in before_conds:
                    record_changes(
                        conditions_to_change_count[key], before_conds[key], conds_now
                    )
                    del before_conds[key]
    return conditions_to_change_count


def most_frequent_changes(env_name, data, key_conditions):
    candidate_conds = enumerate_base_conds(env_name)
    all_conds = enumerate_descriptors(env_name)
    key_cond_proj = {
        key_cond: sample_utils.str_project(key_cond, all_conds)[0]
        for key_cond in key_conditions
    }
    key_cond_rev = {v: k for (k, v) in key_cond_proj.items()}
    key_conds = [key_cond_proj[key_cond] for key_cond in key_conditions]
    conditions_to_change_count = defaultdict(lambda: defaultdict(int))
    for episode in data:
        episode_counts = change_counts(env_name, episode, key_conds, candidate_conds)
        for (key, cond_counts) in episode_counts.items():
            for (cond, count) in cond_counts.items():
                conditions_to_change_count[key][cond] += count
    return {
        key_cond_rev[key]: sorted(
            list(cond_counts.items()), key=lambda pair: pair[1], reverse=True
        )
        for (key, cond_counts) in conditions_to_change_count.items()
    }


def find_most_likely_conditions(
    *,
    envs: str_list = sample_utils.MT10_ENV_NAMES,
    seed=sample_utils.DEFAULT_SEED,
    plan_file: str = "mt50_plans_v1.py",
    out_file: str = "mt10_plans_v2_from_demonstrations.py",
):
    success_rates = {}
    controller_maps = {}
    plans = load_and_parse_plans(plan_file)
    new_plans = {}
    for env_name in envs:
        done = False
        new_plan = {}
        noise_scale = 0.5
        while not done:
            policy = SawyerUniversalV2Policy(env_name=env_name)
            env = sample_utils.make_env(env_name, seed)
            episodes = sample_utils.collect_noisy_episodes(
                10 * [env_name],
                policy,
                n_episodes=100,
                seed=seed,
                noise_scale=noise_scale,
            )
            key_conds = list(plans[env_name].keys())
            freq_changes = most_frequent_changes(env_name, tqdm(episodes), key_conds)
            done = True
            for (key, changes) in freq_changes.items():
                best_goal = None
                best_count = None
                for (cond, count) in changes:
                    if (
                        cond.startswith("the robot's gripper is")
                        and not cond.startswith("the robot's gripper is not")
                        and cond != "the robot's gripper is open"
                        and cond != "the robot's gripper is closed"
                    ):
                        best_goal = cond
                        best_count = count
                        break
                if best_count is None or best_count < 10:
                    if noise_scale > 0.01:
                        noise_scale *= 0.75
                        done = False
                        print(f"NO BEST GOAL FOR {key!r}, retrying")
                        print(f"new noise_scale = {noise_scale}")
                        break
                    else:
                        print(f"OMITTING key {key!r}")
                else:
                    pprint(dict(changes))
                    open_count = dict(changes).get("the robot's gripper is open", 0)
                    close_count = dict(changes).get("the robot's gripper is closed", 0)
                    if open_count > 0.25 * best_count and open_count > close_count:
                        best_goal = f"{best_goal} and the robot's gripper is open"
                    elif close_count > 0.5 * best_count and close_count > open_count:
                        best_goal = f"{best_goal} and the robot's gripper is closed"
                    new_plan[key] = best_goal
            print(plan_str(env_name, new_plan))
            new_plans[env_name] = new_plan
    for (env_name, plan) in new_plans.items():
        print(plan_str(env_name, plan))
    with open(out_file, "w") as f:
        for (env_name, plan) in new_plans.items():
            print(plan_str(env_name, plan), file=f)
            print("\n", file=f)
    return new_plans


if __name__ == "__main__":
    clize.run(find_most_likely_conditions)
