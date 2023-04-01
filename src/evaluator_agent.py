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

import random
from flax import linen as nn
from flax.metrics import tensorboard
from flax.training import train_state
import jax
import jax.numpy as jnp
import ml_collections
import numpy as np
import optax
import pickle
import reverb
import concurrent.futures

from tqdm import tqdm
from metaworld.envs.mujoco.env_dict import MT10_V2
from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE

import sys

sys.path.append("src")

import metaworld_scripted_skills
import train_evaluator
import generate_metaworld_scene_dataset
import embed_prompt
import metaworld_jax_scripted_skills
import easy_process
import embed_prompt
import sample_utils
from sample_utils import make_env, sample_noisy_policy, sample_policy_with_noise_process
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
import jax_utils
from jax_utils import pad_list
from eval_callbacks import SingleProcEvalCallbacks, EvalCallbacks
from datasets import single_env_dataset, grouped_env_dataset


generate_metaworld_scene_dataset.np = jnp
jit_eval_conditions = jax.jit(
    generate_metaworld_scene_dataset.eval_conditions,
    static_argnames=["env_name", "conds", "fuzzy"],
)
# jit_eval_conditions = generate_metaworld_scene_dataset.eval_conditions


def embed_plans(parsed_plans):
    embedded_plans = {}
    for (plan_name, plan) in parsed_plans.items():
        conds = list(plan.keys())
        assert conds, plan_name
        conds_embed = jnp.stack(
            [np.array(embed_prompt.embed_condition(cond)) for cond in conds]
        )
        actions_embed = jnp.stack(
            [np.array(embed_prompt.embed_action(plan[cond])) for cond in conds]
        )
        embedded_plans[plan_name] = {
            "conds": conds_embed,
            "actions": actions_embed,
            "conds_str": conds,
            "actions_str": [plan[cond] for cond in conds],
        }
    return embedded_plans


class CondAgent(nn.Module):
    use_learned_evaluator: bool
    use_learned_scripted_skill: bool
    give_obs_to_learned_scripted_skill: bool
    use_goal_space_primitives: bool
    mix_in_language_space: bool
    plans: dict

    def setup(self):
        self.cond_evaluator = train_evaluator.ConditionEvaluator()
        self.learned_scripted_skill = LearnedScriptedSkill()

    def _compute_goal_space_primitives(self, env_names, low_dim):
        if self.use_learned_evaluator:
            conds_padded, conds_mask = pad_list(
                [
                    jnp.stacK(
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
            logits = jnp.tanh(conds_logits)
        else:
            true_values = []
            for (env_name, obs, plan) in zip(env_names, low_dim, plans):
                true_results = jit_eval_conditions(
                    env_name,
                    generate_metaworld_scene_dataset.enumerate_base_conds(env_name),
                    obs,
                    fuzzy=True,
                )
                true_values.append(true_results)
            padded_true_results, conds_mask = pad_list(true_values)
            logits = 2 * padded_true_results - 1.0
        goal_vecs = []
        for (env_name, plan) in zip(env_names, plans):
            goal_vec = [
                [
                    1.0 if cond in primitive else 0.0
                    for cond in generate_metaworld_scene_dataset.enumerate_base_conds(
                        env_name
                    )
                ]
                for primitive in plan["actions_str"]
            ]
            goal_vecs.append(goal_vec)
        goals_padded, goals_mask = pad_list(goal_vecs)
        return jnp.concatenate([goals_padded, logits], axis=-1), goals_mask

    def __call__(self, env_names, low_dim):
        info = {}
        plans = [self.plans[env_name] for env_name in env_names]
        if self.use_goal_space_primitives:
            assert self.mix_in_language_space
        if self.use_learned_evaluator:
            conds_padded, conds_mask = pad_list([plan["conds"] for plan in plans])
            conds_logits = self.cond_evaluator(low_dim, conds_padded)
            logits = 10 * jnp.tanh(conds_logits)
        else:
            true_values = []
            for (env_name, obs, plan) in zip(env_names, low_dim, plans):
                true_results = jit_eval_conditions(
                    env_name, plan["conds_str"], obs, fuzzy=True
                )
                true_values.append(true_results)
            padded_true_results, conds_mask = pad_list(true_values)
            logits = 10 * padded_true_results - 5
        scripted_skill_weights = nn.softmax(logits, axis=1, where=conds_mask, initial=0)
        info["logits"] = logits
        info["scripted_skill_weights"] = scripted_skill_weights
        scripted_skill_weights /= scripted_skill_weights.sum(axis=1)[0]
        scripted_skill_outputs = []
        if self.mix_in_language_space:
            assert self.use_learned_scripted_skill
            if self.use_goal_space_primitives:
                primitive_reprs, primitive_mask = self._compute_goal_space_primitives(
                    env_names, low_dim
                )
            else:
                embedded_scripted_skill_names = [plan["actions"] for plan in plans]
                primitive_reprs, primitive_mask = pad_list(
                    embedded_scripted_skill_names
                )
            action_embed = jnp.einsum(
                "ij,ijk->ik", scripted_skill_weights, primitive_reprs
            )
            if self.give_obs_to_learned_scripted_skill:
                actions, scripted_skill_info = self.learned_scripted_skill(
                    action_embed, low_dim
                )
            else:
                actions, scripted_skill_info = self.learned_scripted_skill(action_embed)
        else:
            if self.use_learned_scripted_skill:
                scripted_skill_outputs = []
                for (obs, plan) in zip(low_dim, plans):
                    if self.give_obs_to_learned_scripted_skill:
                        action, scripted_skill_info = self.learned_scripted_skill(
                            plan["actions"],
                            jnp.array([obs for action_embed in plan["actions"]]),
                        )
                    else:
                        action, scripted_skill_info = self.learned_scripted_skill(
                            plan["actions"],
                        )
                    scripted_skill_outputs.append(action)
                scripted_skill_outputs, scripted_skill_mask = pad_list(
                    scripted_skill_outputs
                )
                actions = jnp.einsum(
                    "ij,ijk->ik", scripted_skill_weights, scripted_skill_outputs
                )
            else:
                for (env_name, obs, plan) in zip(env_names, low_dim, plans):
                    parsed_obs = metaworld_jax_scripted_skills.parse_obs(obs)
                    metaworld_scripted_skills.np = jnp
                    scripted_skill_outputs.append(
                        [
                            metaworld_scripted_skills.run_scripted_skill(
                                name, parsed_obs
                            )
                            for name in plan["actions_str"]
                        ]
                    )
                scripted_skill_outputs, _ = pad_list(scripted_skill_outputs)
                actions = jnp.einsum(
                    "ij,ijk->ik", scripted_skill_weights, scripted_skill_outputs
                )
        return actions, info

    def as_policy(self, env_name, state):
        return CondAgentPolicy(env_name=env_name, state=state, cond_agent=self)


class LearnedScriptedSkill(nn.Module):
    def setup(self):
        self.language_reencoder = nn.Sequential(
            [
                nn.Dense(64),
                nn.relu,
                nn.Dense(64),
                nn.relu,
                nn.Dense(64),
            ]
        )
        self.action_model = nn.Sequential(
            [
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(64),
                nn.relu,
                nn.Dense(32),
                nn.relu,
                nn.Dense(4),
            ]
        )

    def __call__(self, encoded_language_actions, low_dim=None):
        info = {}
        reencoded_language = self.language_reencoder(encoded_language_actions)
        if low_dim is not None:
            obs_and_lang_actions = jnp.concatenate(
                [low_dim, reencoded_language], axis=-1
            )
            actions = self.action_model(obs_and_lang_actions)
        else:
            actions = self.action_model(reencoded_language)
        return actions, info


@dataclass
class CondAgentPolicy:

    env_name: str or None
    state: train_state.TrainState
    cond_agent: CondAgent

    def get_action(self, low_dim, env_name=None):
        env_name = env_name or self.env_name
        assert env_name
        actions, infos = self.get_actions(np.array([low_dim]), [env_name])
        return actions[0], {k: v[0] for (k, v) in infos.items()}

    def get_actions(self, observations, env_names):
        action, info = run_cond_agent(self.state, tuple(env_names), observations)

        # for (k, v) in info.items():
        # print(k, v)

        return np.asarray(action), info


@partial(jax.jit, static_argnames=["env_names"])
def run_cond_agent(state, env_names, observations):
    return state.apply_fn(state.params, env_names, observations)


@partial(jax.jit, static_argnames=["env_names"])
def apply_model(state, env_names, low_dim, targets):
    def loss_fn(params):
        actions, info = state.apply_fn(params, env_names, low_dim)
        loss = jnp.mean(optax.l2_loss(actions, targets))
        return loss, actions

    grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
    (loss, actions), grads = grad_fn(state.params)
    return (
        grads,
        loss,
        {
            "actions_mean": jnp.mean(actions),
            "actions_var": jnp.var(actions),
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
    return (tuple(env_names), jnp.array(observations)), jnp.array(actions)


def load_best_evaluator_params():
    with open(os.path.expanduser("~/data/best_evaluator.pkl"), "rb") as f:
        cond_eval_state = pickle.load(f)
    return cond_eval_state["params"]


def zeroshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    test_envs: str_list = MT50_ENV_NAMES,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    batch_size=4,
    noise_scale=0.1,
    language_space_mixing=True,
    use_noise=True,
    give_obs_to_learned_scripted_skill=True,
    use_goal_space_primitives=False,
    plan_file,
    out_file,
):
    from generate_mt10_plans import load_and_parse_plans

    if use_noise:
        data = grouped_env_dataset(envs=train_envs, n_timesteps=n_timesteps, seed=seed)
    else:
        data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
    parsed_plans = load_and_parse_plans(plan_file)
    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=language_space_mixing,
        use_learned_scripted_skill=True,
        give_obs_to_learned_scripted_skill=give_obs_to_learned_scripted_skill,
        use_goal_space_primitives=use_goal_space_primitives,
        plans=embed_plans(parsed_plans),
    )
    callbacks = SingleProcEvalCallbacks(
        seed, train_envs + test_envs, cond_agent, output_filename=out_file
    )
    # callbacks.step_period = 100
    jax_utils.fit_model(
        cond_agent,
        data,
        apply_model,
        "cond_agent",
        batch_size=batch_size,
        preprocess=preprocess,
        seed=seed,
        n_epochs=500,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    embed_prompt.save_cache()
    print("Done saving cache")


def fewshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    fewshot_timesteps=500,
    language_space_mixing=True,
    use_noise=True,
    give_obs_to_learned_scripted_skill=True,
    use_goal_space_primitives=False,
    plan_file,
    out_file,
):
    from generate_mt10_plans import load_and_parse_plans

    parsed_plans = load_and_parse_plans(plan_file)
    print(parsed_plans, file=sys.stderr)
    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=language_space_mixing,
        use_learned_scripted_skill=True,
        give_obs_to_learned_scripted_skill=give_obs_to_learned_scripted_skill,
        use_goal_space_primitives=use_goal_space_primitives,
        plans=embed_plans(parsed_plans),
    )
    callbacks = SingleProcEvalCallbacks(
        seed,
        [target_env],
        cond_agent,
        base_infos={
            "target_task": target_env,
        },
        output_filename=out_file,
    )
    train_and_evaluate_fewshot_with_callbacks(
        callbacks=callbacks,
        cond_agent=cond_agent,
        train_envs=train_envs,
        target_env=target_env,
        seed=seed,
        n_timesteps=n_timesteps,
        fewshot_timesteps=fewshot_timesteps,
        use_noise=use_noise,
    )


def fewshot_process(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    fewshot_timesteps=500,
    give_obs_to_learned_scripted_skill=True,
    use_goal_space_primitives=False,
    parent,
):
    from generate_mt10_plans import load_and_parse_plans

    sys.stdout = open(expanduser(f"~/data/{target_env}.stdout"), "w")
    sys.stderr = open(expanduser(f"~/data/{target_env}.stderr"), "w")

    embedded_plans = {}
    parsed_plans = load_and_parse_plans("mt50_plans.py")
    print("Embedding plans...")
    for (plan_name, plan) in parsed_plans.items():
        conds = list(plan.keys())
        conds_embed = jnp.stack(
            [np.array(embed_prompt.embed_condition(cond)) for cond in conds]
        )
        actions_embed = jnp.stack(
            [np.array(embed_prompt.embed_action(plan[cond])) for cond in conds]
        )
        embedded_plans[plan_name] = {
            "conds": conds_embed,
            "actions": actions_embed,
            "conds_str": conds,
            "actions_str": [plan[cond] for cond in conds],
        }
    print("Done embedding plans")

    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=True,
        use_learned_scripted_skill=True,
        give_obs_to_learned_scripted_skill=give_obs_to_learned_scripted_skill,
        use_goal_space_primitives=use_goal_space_primitives,
        plans=embedded_plans,
    )
    callbacks = SingleProcEvalCallbacks(
        seed,
        [target_env],
        cond_agent,
        base_infos={
            "target_task": target_env,
        },
        results_proc=parent,
    )
    callbacks.step_period = 30
    try:
        train_and_evaluate_fewshot_with_callbacks(
            callbacks=callbacks,
            cond_agent=cond_agent,
            train_envs=train_envs,
            target_env=target_env,
            seed=seed,
            n_timesteps=n_timesteps,
            fewshot_timesteps=fewshot_timesteps,
        )
    except Exception as exc:
        print(exc)
        raise exc


def train_and_eval_all_fewshot_parallel(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_envs: str_list = MT50_ENV_NAMES,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e4,
    fewshot_timesteps=500,
):
    workdir = expanduser(f"~/data/train_and_eval_all_fewshot_seed={seed}")
    n_evals = 101
    summary_writer = tensorboard.SummaryWriter(workdir)
    scope = easy_process.Scope()
    try:
        workers = []
        for env_name in target_envs:
            print(f"Starting worker for task {1+len(workers)}/{len(target_envs)}")
            workers.append(
                easy_process.Subprocess(
                    fewshot_process,
                    kwargs=dict(
                        train_envs=train_envs,
                        target_env=env_name,
                        seed=seed,
                        n_timesteps=n_timesteps,
                        fewshot_timesteps=fewshot_timesteps,
                    ),
                    scope=scope,
                )
            )
            # Sampling uses a lot of memory, so start processes slowly
            time.sleep(10)
        print("#" * 30, "ALL WORKERS STARTED", "#" * 30)
        datapoints = []
        successes = defaultdict(list)
        for i in tqdm(range(n_evals)):
            success_rates = {}
            rewards = {}
            for worker in workers:
                info = worker.recv(block=True)
                env_name = info["target_task"]
                success_rates[env_name] = info[f"{env_name}/SuccessRate"]
                rewards[env_name] = info[f"{env_name}/RewardMean"]
                summary_writer.scalar(
                    f"{env_name}/SuccessRate", success_rates[env_name], i
                )
                summary_writer.scalar(
                    f"{env_name}/RewardMean", info[f"{env_name}/RewardMean"], i
                )
            print("reward_means =", rewards)
            print("success_rates =", success_rates)
            for threshold in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                tasks_at_success_rate = [
                    env_name
                    for env_name in target_envs
                    if success_rates[env_name] >= threshold
                ]
                summary_writer.scalar(
                    f"TasksAtSuccessRate/success_rate:{threshold}",
                    len(tasks_at_success_rate),
                    i,
                )
            summary_writer.flush()
    finally:
        scope.close()


def train_and_eval_all_fewshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e4,
    fewshot_timesteps=500,
):
    for env_name in target_envs:
        fewshot(
            train_envs=train_envs,
            target_env=env_name,
            seed=seed,
            n_timesteps=n_timesteps,
            fewshot_timesteps=fewshot_timesteps,
        )


def train_and_evaluate_fewshot_with_callbacks(
    *,
    callbacks,
    cond_agent,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    fewshot_timesteps=500,
    use_noise=True,
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
        return (tuple(env_names), jnp.array(observations)), jnp.array(actions)

    if use_noise:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed
        )
        target_data = single_env_dataset(
            env_name=target_env, n_timesteps=fewshot_timesteps, seed=seed
        )
    else:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
        target_data = single_env_dataset(
            env_name=target_env,
            n_timesteps=fewshot_timesteps,
            seed=seed,
            noise_scales=[0.0],
        )
    jax_utils.fit_model_multisource(
        model=cond_agent,
        sources=[base_data, target_data],
        source_repeats=source_repeats,
        apply_model=apply_model,
        model_name=f"cond_agent_fewshot_task={target_env}",
        preprocess=preprocess_fewshot,
        seed=seed,
        n_epochs=500,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    embed_prompt.save_cache()
    print("Done saving cache")


if __name__ == "__main__":
    # import multiprocessing as mp

    # mp.set_start_method("spawn")
    clize.run(zeroshot, fewshot)
