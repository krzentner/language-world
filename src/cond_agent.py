import collections
import time
import json
from collections import defaultdict
from dataclasses import dataclass
import clize
from functools import partial
import os
import typing
import cloudpickle
from os.path import expanduser

import torch
from torch import nn
from torch.nn import functional as F
import numpy as np

import random
import numpy as np
import pickle

from tqdm import tqdm
from metaworld.envs.mujoco.env_dict import MT10_V2
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE

import sys

sys.path.append("src")

import generate_metaworld_scene_dataset
import embed_prompt
import metaworld_scripted_skills
import easy_process
import embed_prompt
import sample_utils
from sample_utils import make_env, sample_noisy_policy, sample_policy_with_noise_process
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
import pytorch_utils
from pytorch_utils import pad_list
from eval_callbacks import SingleProcEvalCallbacks, EvalCallbacks
from datasets import single_env_dataset, grouped_env_dataset
from plan_encoding import load_plan_file
from constants import MT10_ENV_NAMES, MT50_ENV_NAMES, N_EPOCHS, N_BASE_TIMESTEPS
import lightning_utils


def embed_plans(parsed_plans):
    embedded_plans = {}
    for plan_name, plan in parsed_plans.items():
        conds = [cond for (skill, cond) in plan]
        skills = [skill for (skill, cond) in plan]
        assert conds, plan_name
        conds_embed = np.stack(
            [np.array(embed_prompt.embed_condition(cond)) for cond in conds]
        )
        skill_embed = np.stack(
            [np.array(embed_prompt.embed_action(skill)) for skill in skills]
        )
        embedded_plans[plan_name] = {
            "conds": conds_embed,
            "skills": skill_embed,
            "conds_str": conds,
            "skill_str": skills,
        }
    return embedded_plans


class CondAgent(nn.Module):
    def __init__(
        self,
        *,
        use_learned_evaluator: bool = False,
        use_learned_skills: bool = True,
        give_obs_to_learned_skill: bool = True,
        use_goals_as_skills: bool = False,
        mix_in_language_space: bool = False,
        plans,
    ):
        super().__init__()
        self.use_learned_evaluator = use_learned_evaluator
        self.use_learned_skills = use_learned_skills
        self.give_obs_to_learned_skill = give_obs_to_learned_skill
        self.use_goals_as_skills = use_goals_as_skills
        self.mix_in_language_space = mix_in_language_space
        self.plans = plans
        self.skill_decoder = SkillDecoder()
        if self.use_learned_evaluator:
            import train_evaluator

            self.cond_evaluator = train_evaluator.ConditionEvaluator()

    def _compute_goal_space_primitives(self, env_names, low_dim):
        if self.use_learned_evaluator:
            conds_padded, conds_mask = pad_list(
                [
                    torch.stacK(
                        [
                            embed_prompt.embed_condition(cond)
                            for cond in generate_metaworld_scene_dataset.enumerate_base_conds(
                                env_name
                            )
                        ]
                    )
                    for env_name in env_names
                ]
            )
            conds_logits = self.cond_evaluator(low_dim, conds_padded)
            logits = torch.tanh(conds_logits)
        else:
            true_values = []
            for env_name, obs, plan in zip(env_names, low_dim, plans):
                true_results = generate_metaworld_scene_dataset.eval_conditions(
                    env_name,
                    generate_metaworld_scene_dataset.enumerate_base_conds(env_name),
                    obs,
                    fuzzy=True,
                )
                true_values.append(true_results)
            padded_true_results, conds_mask = pad_list(true_values)
            logits = 2 * padded_true_results - 1.0
        goal_vecs = []
        for env_name, plan in zip(env_names, plans):
            goal_vec = [
                [
                    1.0 if cond in primitive else 0.0
                    for cond in generate_metaworld_scene_dataset.enumerate_base_conds(
                        env_name
                    )
                ]
                for primitive in plan["skill_str"]
            ]
            goal_vecs.append(goal_vec)
        goals_padded, goals_mask = pad_list(goal_vecs)
        return torch.concatenate([goals_padded, logits], dim=-1), goals_mask

    def __call__(self, env_names, low_dim):
        info = {}
        device = self.skill_decoder.decoder[0].weight.device
        plans = [self.plans[env_name] for env_name in env_names]
        if self.use_goals_as_skills:
            assert self.mix_in_language_space
        if self.use_learned_evaluator:
            conds_padded, conds_mask = pad_list([plan["conds"] for plan in plans])
            conds_logits = self.cond_evaluator(low_dim, conds_padded)
            logits = 10 * torch.tanh(conds_logits)
        else:
            true_values = []
            for env_name, obs, plan in zip(env_names, low_dim, plans):
                true_results = generate_metaworld_scene_dataset.eval_conditions(
                    env_name, plan["conds_str"], np.asarray(obs.cpu()), fuzzy=True
                )
                true_values.append(true_results)
            padded_true_results, conds_mask = pad_list(true_values)
            logits = 10 * padded_true_results.type(torch.float32).to(device) - 5
        # scripted_skill_weights = F.softmax(logits, dim=1, where=conds_mask, initial=0)
        logits[conds_mask == 0] = float("-inf")
        scripted_skill_weights = F.softmax(logits, dim=1)
        info["logits"] = logits
        info["scripted_skill_weights"] = scripted_skill_weights
        scripted_skill_weights /= scripted_skill_weights.sum(dim=1)[0]
        scripted_skill_outputs = []
        if self.mix_in_language_space:
            assert self.use_learned_skills
            if self.use_goals_as_skills:
                primitive_reprs, primitive_mask = self._compute_goal_space_primitives(
                    env_names, low_dim
                )
            else:
                embedded_scripted_skill_names = [plan["skills"] for plan in plans]
                primitive_reprs, primitive_mask = pad_list(
                    embedded_scripted_skill_names
                )
            skill_embed = torch.einsum(
                "ij,ijk->ik", scripted_skill_weights.to(device), primitive_reprs.to(device)
            )
            if self.give_obs_to_learned_skill:
                skills, scripted_skill_info = self.skill_decoder(skill_embed, low_dim)
            else:
                skills, scripted_skill_info = self.skill_decoder(skill_embed)
        else:
            if self.use_learned_skills:
                scripted_skill_outputs = []
                for obs, plan in zip(low_dim, plans):
                    if self.give_obs_to_learned_skill:
                        action, scripted_skill_info = self.skill_decoder(
                            plan["skills"],
                            torch.stack([obs for skill_embed in plan["skills"]]),
                        )
                    else:
                        action, scripted_skill_info = self.skill_decoder(
                            plan["skills"],
                        )
                    scripted_skill_outputs.append(action)
                scripted_skill_outputs, scripted_skill_mask = pad_list(
                    scripted_skill_outputs
                )
                skills = torch.einsum(
                    "ij,ijk->ik", scripted_skill_weights, scripted_skill_outputs
                )
            else:
                for env_name, obs, plan in zip(env_names, low_dim, plans):
                    parsed_obs = metaworld_scripted_skills.parse_obs(obs)
                    scripted_skill_outputs.append(
                        [
                            metaworld_scripted_skills.run_scripted_skill(
                                name, parsed_obs
                            )
                            for name in plan["skill_str"]
                        ]
                    )
                scripted_skill_outputs, _ = pad_list(scripted_skill_outputs)
                skills = torch.einsum(
                    "ij,ijk->ik", scripted_skill_weights, scripted_skill_outputs
                )
        return skills, info

    @torch.jit.ignore
    def as_policy(self, env_name):
        return CondAgentPolicy(env_name=env_name, agent=self)


class SkillDecoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.language_reencoder = nn.Sequential(
            nn.LazyLinear(64),
            nn.ReLU(),
            nn.LazyLinear(64),
            nn.ReLU(),
            nn.LazyLinear(64),
        )
        self.decoder = nn.Sequential(
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(64),
            nn.ReLU(),
            nn.LazyLinear(32),
            nn.ReLU(),
            nn.LazyLinear(4),
        )

    def __call__(self, encoded_language_skills, low_dim=None):
        info = {}
        reencoded_language = self.language_reencoder(encoded_language_skills)
        if low_dim is not None:
            obs_and_lang_skills = torch.concatenate(
                [low_dim, reencoded_language], dim=-1
            )
            actions = self.decoder(obs_and_lang_skills)
        else:
            actions = self.decoder(reencoded_language)
        return actions, info


@dataclass
class CondAgentPolicy:
    env_name: str or None
    agent: CondAgent

    def get_action(self, low_dim, env_name=None):
        env_name = env_name or self.env_name
        assert env_name
        actions, infos = self.get_actions(np.array([low_dim]), [env_name])
        return actions[0], {k: v[0] for (k, v) in infos.items()}

    def get_actions(self, observations, env_names=None):
        if env_names is None:
            env_names = [self.env_name] * len(observations)
        with torch.no_grad():
            actions, infos = self.agent(
                np.array(env_names),
                torch.as_tensor(np.array(observations), dtype=torch.float32),
            )
        return np.asarray(actions.cpu()), infos


def loss_function(agent, env_names, low_dim, targets):
    actions, info = agent(env_names, low_dim)
    loss = F.mse_loss(actions, targets)
    return (
        loss,
        {
            "actions_mean": torch.mean(actions),
            "actions_var": torch.var(actions),
        },
    )


def preprocess(batch):
    env_names = []
    observations = []
    actions = []
    for stack in batch:
        for data in stack:
            env_names.append(data["env_name"])
            observations.append(data["observation"])
            actions.append(data["action"])
    return (
        tuple(env_names),
        torch.tensor(np.array(observations), dtype=torch.float32),
    ), torch.tensor(np.array(actions), dtype=torch.float32)


def load_best_evaluator_params():
    with open(os.path.expanduser("~/data/best_evaluator.pkl"), "rb") as f:
        cond_eval_state = pickle.load(f)
    return cond_eval_state["params"]


def zeroshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    test_envs: str_list = MT50_ENV_NAMES,
    seed=pytorch_utils.DEFAULT_SEED,
    n_timesteps=N_BASE_TIMESTEPS,
    batch_size=4,
    noise_scale=0.1,
    language_space_mixing=True,
    use_noise=False,
    give_obs_to_learned_skill=True,
    use_goals_as_skills=False,
    n_epochs=N_EPOCHS,
    plan_file,
    out_file,
):
    if use_noise:
        data = grouped_env_dataset(
            envs=train_envs,
            n_timesteps=n_timesteps,
            seed=seed,
            noise_scales=[noise_scale],
        )
    else:
        data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
    parsed_plans = load_plan_file(plan_file)
    callbacks = SingleProcEvalCallbacks(
        seed, train_envs + test_envs, output_filename=out_file
    )

    def create_model(example_inputs):
        agent = CondAgent(
            use_learned_evaluator=False,
            mix_in_language_space=language_space_mixing,
            use_learned_skills=True,
            give_obs_to_learned_skill=give_obs_to_learned_skill,
            use_goals_as_skills=use_goals_as_skills,
            plans=embed_plans(parsed_plans),
        )
        with torch.no_grad():
            agent(*example_inputs)
        return agent

    # callbacks.step_period = 100
    lightning_utils.fit_model(
        data=data,
        create_model=create_model,
        loss_function=loss_function,
        model_name="cond_agent_zeroshot",
        batch_size=batch_size,
        preprocess=preprocess,
        seed=seed,
        n_epochs=n_epochs,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    embed_prompt.save_cache()
    print("Done saving cache")


def oneshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_task: str,
    seed=pytorch_utils.DEFAULT_SEED,
    n_timesteps=N_BASE_TIMESTEPS,
    fewshot_timesteps=500,
    language_space_mixing=True,
    use_noise=True,
    give_obs_to_learned_skill=True,
    use_goals_as_skills=False,
    n_epochs: int = N_EPOCHS,
    plan_file,
    out_file,
):
    parsed_plans = load_plan_file(plan_file)
    agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=language_space_mixing,
        use_learned_skills=True,
        give_obs_to_learned_skill=give_obs_to_learned_skill,
        use_goals_as_skills=use_goals_as_skills,
        plans=embed_plans(parsed_plans),
    )
    callbacks = SingleProcEvalCallbacks(
        seed,
        [target_task],
        base_infos={
            "target_task": target_task,
        },
        output_filename=out_file,
    )
    train_and_evaluate_fewshot_with_callbacks(
        callbacks=callbacks,
        agent=agent,
        train_envs=train_envs,
        target_task=target_task,
        seed=seed,
        n_timesteps=n_timesteps,
        fewshot_timesteps=fewshot_timesteps,
        use_noise=use_noise,
        n_epochs=n_epochs,
    )


def train_and_evaluate_fewshot_with_callbacks(
    *,
    callbacks,
    agent,
    train_envs: str_list = MT10_ENV_NAMES,
    target_task: str,
    seed=pytorch_utils.DEFAULT_SEED,
    n_timesteps=N_BASE_TIMESTEPS,
    fewshot_timesteps=500,
    use_noise=True,
    n_epochs=N_EPOCHS,
):
    # batch_size is basically source_repeats[0] * train_envs + source_repeats[1]
    source_repeats = [2, 20]

    def preprocess_fewshot(batch):
        env_names = []
        observations = []
        actions = []
        base_stacks = batch[: source_repeats[0]]
        target_stack = batch[source_repeats[0] :]
        assert len(target_stack) == source_repeats[1]
        for stack in base_stacks + [target_stack]:
            for data in stack:
                env_names.append(data["env_name"])
                observations.append(data["observation"])
                actions.append(data["action"])
        return (
            tuple(env_names),
            torch.tensor(np.array(observations), dtype=torch.float32),
        ), torch.tensor(np.array(actions), dtype=torch.float32)

    if use_noise:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed
        )
        target_data = single_env_dataset(
            env_name=target_task, n_timesteps=fewshot_timesteps, seed=seed
        )
    else:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
        target_data = single_env_dataset(
            env_name=target_task,
            n_timesteps=fewshot_timesteps,
            seed=seed,
            noise_scales=[0.0],
        )

    def create_model(example_inputs):
        with torch.no_grad():
            agent(*example_inputs)
        return agent

    lightning_utils.fit_model_multisource(
        create_model=create_model,
        loss_function=loss_function,
        sources=[base_data, target_data],
        source_repeats=source_repeats,
        model_name=f"cond_agent_fewshot_task={target_task}",
        preprocess=preprocess_fewshot,
        seed=seed,
        n_epochs=n_epochs,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    embed_prompt.save_cache()
    print("Done saving cache")


if __name__ == "__main__":
    # import multiprocessing as mp

    # mp.set_start_method("spawn")
    clize.run(zeroshot, oneshot)
