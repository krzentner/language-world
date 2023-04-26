from dataclasses import dataclass
from typing import Dict, List, Tuple, Union
import random
import numpy as np

from generate_metaworld_scene_dataset import eval_conditions, enumerate_descriptors
from metaworld_scripted_skills import (
    parse_obs,
    run_scripted_skill,
    nearest_skill,
    str_project,
)


@dataclass
class ScriptedCondAgent:
    cond_to_scripted_skill: List[Tuple[str, str]]
    env_name: str

    scripted_skill_choice_prob: float = 1.0

    # If not None, mix actions
    skill_mix_base_weight: Union[float, None] = None

    def get_action(self, observation):
        obs = parse_obs(observation)
        candidate_scripted_skills = [
            skill
            for (cond, skill) in self.cond_to_scripted_skill
            if eval_conditions(self.env_name, (cond,), obs)[0]
        ]
        if (
            candidate_scripted_skills
            and random.uniform(0, 1) < self.scripted_skill_choice_prob
        ):
            scripted_skill_name = random.choice(candidate_scripted_skills)
        else:
            scripted_skill_name = random.choice(
                [skill for (_, skill) in self.cond_to_scripted_skill]
            )
        info = {}
        info["scripted_skill_name"] = scripted_skill_name
        info["candidate_scripted_skills"] = list(set(candidate_scripted_skills))
        if self.skill_mix_base_weight:
            weights = np.array(
                [
                    1.0
                    if eval_conditions(self.env_name, (cond,), obs)[0]
                    else self.skill_mix_base_weight
                    for (cond, _) in self.cond_to_scripted_skill
                ]
            )
            weights /= weights.sum()
            actions = np.array(
                [
                    run_scripted_skill(skill, obs)
                    for (_, skill) in self.cond_to_scripted_skill
                ]
            )
            weighted_action = np.einsum("i,ik->k", weights, actions)
            return weighted_action, info
        else:
            return run_scripted_skill(scripted_skill_name, obs), info

    def get_actions(self, observations):
        actions = []
        infos = []
        for observation in observations:
            action, info = self.get_action(observation)
            actions.append(action)
            infos.append(info)
        return np.array(actions), {
            k: np.array([info[k] for info in infos]) for k in infos[0].keys()
        }


def project_plan(plan: List[Tuple[str, str]], task: str) -> List[Tuple[str, str]]:
    out = []
    possible_conditions = enumerate_descriptors(task)
    for (cond, skill) in plan:
        cond_projected = str_project(cond, possible_conditions)[0]
        out.append((cond_projected, nearest_skill(target_task=task, skill=skill)))
    return out


def run_plan_file(plan_file, out_file, *, task: str, seed=1111):
    from plan_encoding import decode
    from sample_utils import eval_policy
    from tqdm import tqdm
    import json

    plans = decode(plan_file, encoding="guess", task=task)
    success_rates = {}
    rewards = {}
    plan = plans.get(task, None)
    if plan is not None:
        plan_projected = project_plan(plan, task)
        policy = ScriptedCondAgent(env_name=task, cond_to_scripted_skill=plan_projected)
        success_rates[task], rewards[task] = eval_policy(policy, task, seed=seed)
    success_rates_json = json.dumps(success_rates, indent=True)
    print("Success rates:")
    print(success_rates_json)
    with open(out_file, "w") as out_f:
        out_f.write(success_rates_json)


if __name__ == "__main__":
    import clize

    clize.run(run_plan_file)
