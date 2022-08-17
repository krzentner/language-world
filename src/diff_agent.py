import clize
import shutil
import numpy as np
from sample_utils import str_project
from dataclasses import dataclass
from metaworld_controllers import parse_obs, run_controller, CONTROLLERS
from generate_metaworld_scene_dataset import eval_conditions, enumerate_descriptors
from generate_mt10_plans import load_and_parse_plans
import sample_utils
import random
import json
from sample_utils import MT50_ENV_NAMES, make_env, collect_noisy_episodes, evaluate_policy, sample_noisy_policy
from render_policy import render_policy
from run_utils import str_list
from tqdm import tqdm

PRIMITIVE_NAMES = list(CONTROLLERS.keys())
PROJ_CACHE = {}

@dataclass
class DiffAgent:
    conds: list[str]
    primitives: list[str]
    env_name: str
    controller_choice_prob: float = 1.0

    def __post_init__(self):
        possible_conds = enumerate_descriptors(self.env_name)
        self.conds = [str_project(cond, possible_conds)[0] for cond in self.conds]

    def get_action(self, observation):
        obs = parse_obs(observation)
        cond_results = eval_conditions(self.env_name, self.conds, obs, fuzzy=True)
        candidate_controllers = [
            prim
            for (truth_value, prim) in zip(cond_results, self.primitives)
            if truth_value > 0
        ]
        if candidate_controllers and np.random.uniform() < self.controller_choice_prob:
            controller_name = random.choice(candidate_controllers)
        else:
            controller_name = random.choice(self.primitives)
        info = {}
        info["controller_name"] = controller_name
        info["candidate_controllers"] = list(set(candidate_controllers))
        if controller_name not in PROJ_CACHE:
            PROJ_CACHE[controller_name] = str_project(controller_name, PRIMITIVE_NAMES)[0]
        chosen_controller = PROJ_CACHE[controller_name]
        info["chosen_controller"] = chosen_controller
        return run_controller(chosen_controller, obs), info


def eval_diff_agent(
    *,
    seed=sample_utils.DEFAULT_SEED,
    env_names: str_list = MT50_ENV_NAMES,
    out_success: str,
    out_avg_reward: str,
    render_output_dir: str,
):
    success_rates = {}
    rewards = {}
    plans = load_and_parse_plans('mt50_plans.py')
    for env_name in env_names:
        plan = plans[env_name]
        conds = list(plan.keys())
        primitives = [plan[cond] for cond in conds]
        policy = DiffAgent(conds, primitives, env_name)
        policy_name = "diff_agent"
        print(env_name)
        policy.env_name = env_name
        env = make_env(env_name, seed)
        success, rew = evaluate_policy(
            env_name,
            # [sample_noisy_policy(env, policy, 0.05) for _ in tqdm(range(20))]
            collect_noisy_episodes(
                20 * [env_name], policy, seed=seed, n_episodes=100, noise_scale=0.05
            ),
        )
        success_rates[env_name] = success
        rewards[env_name] = rew
        for i in range(20):
            render_success, _ = render_policy(
                    env, policy, f"{render_output_dir}/{env_name}-{policy_name}-{i}.mp4"
            )
            if render_success:
                shutil.copy(
                    f"{render_output_dir}/{env_name}-{policy_name}-{i}.mp4",
                    f"{render_output_dir}//{env_name}-{policy_name}-success.mp4",
                )
                print(f"Rendered successful episode for {env_name}")
                break
            elif success == 0:
                print(f"Skipping additional renders of {env_name}")
                break
            elif i == 19:
                print(f"Could not render successful episode for {env_name}")

    print(success_rates)
    print(rewards)
    with open(out_success, 'w') as f:
        json.dump(succcess_rates, f)
    with open(out_avg_reward, 'w') as f:
        json.dump(rewards, f)

if __name__ == '__main__':
    clize.run(eval_diff_agent)
