import collections
from collections import defaultdict
from dataclasses import dataclass
import clize
from functools import partial
import os
import typing
import cloudpickle

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

import metaworld_controllers
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs
import train_evaluator
import generate_metaworld_scene_dataset
import embed_prompt
import metaworld_jax_controllers
import easy_process
import embed_prompt
import sample_utils
from sample_utils import make_env, sample_noisy_policy, sample_policy_with_noise_process
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
from ou_process import OUProcess
import jax_utils

import pickle

ENV_NAME_TO_PLAN_NAME = {
    "drawer-close": "close_drawer",
    "drawer-open": "open_drawer",
    "peg-insert-side": "insert_peg_right_into_slot",
    "door-open": "open_door",
    "pick-place": "pick_puck_and_hold_at_target",
    "button-press-topdown": "press_button_from_above",
    "push": "slide_puck_to_target",
    "window-close": "slide_window_closed_right",
    "window-open": "slide_window_open_left",
    "reach": "reach_for_target",
}


def pad_list(seq, max_len=None):
    if max_len is None:
        max_len = max(len(s) for s in seq)
    zero = jnp.zeros(seq[0][0].shape)
    padded = jnp.array(
        [[s[i] if len(s) > i else zero for i in range(max_len)] for s in seq]
    )
    mask = jnp.array([[1 if len(s) > i else 0 for i in range(max_len)] for s in seq])
    return padded, mask


parsed_plans_2 = {
    "reach": {
        "reach target is mostly below the robot's gripper": "reach to goal",
        "reach target is not right of the robot's gripper": "reach to goal",
    },
    "push": {
        "puck is not below the robot's gripper": "put the gripper above the puck",
        "the robot's gripper is not above puck": "put the gripper above the puck",
        "puck is below the robot's gripper and puck is not near the robot's gripper": "push the gripper into the puck",
        "puck is below the robot's gripper and the robot's gripper is not near puck": "push the gripper into the puck",
        "puck is near the robot's gripper and puck is below the robot's gripper": "slide the puck to the goal",
        "puck is near the robot's gripper and the robot's gripper is above puck": "slide the puck to the goal",
    },
    "pick-place": {
        "puck is not below the robot's gripper": "place gripper above puck",
        "the robot's gripper is not above puck": "place gripper above puck",
        "puck is below the robot's gripper and puck is not around the robot's gripper": "drop gripper around puck",
        "puck is not around the robot's gripper and puck is below the robot's gripper": "drop gripper around puck",
        "puck is around the robot's gripper and gripper is open": "close gripper around puck",
        "gripper is open and puck is around the robot's gripper": "close gripper around puck",
        "gripper is closed": "place puck at goal",
        "puck is mostly below target location and gripper is closed": "place puck at goal",
    },
    "door-open": {
        "door handle is not almost vertically aligned with the robot's gripper": "put gripper above door handle",
        "the robot's gripper is not almost vertically aligned with door handle": "put gripper above door handle",
        "door handle is left of the robot's gripper and gripper is closed": "put gripper around door handle",
        "the robot's gripper is right of door handle and gripper is closed": "put gripper around door handle",
        "door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper": "push door closed",
        "door handle is vertically aligned with the robot's gripper and the robot's gripper is not right of door handle": "push door closed",
    },
    "drawer-open": {
        "drawer handle is not vertically aligned with the robot's gripper": "put gripper above drawer handle",
        "the robot's gripper is not vertically aligned with drawer handle": "put gripper above drawer handle",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is around drawer handle": "pull away from drawer",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is around drawer handle": "pull away from drawer",
    },
    "drawer-close": {
        "gripper is open": "put the gripper in front of the drawer",
        "drawer handle is vertically aligned with the robot's gripper and gripper is open": "put the gripper in front of the drawer",
        "drawer handle is below the robot's gripper": "put the gripper above the drawer handle",
        "the robot's gripper is above drawer handle": "put the gripper above the drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper": "grab drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with drawer handle": "grab drawer handle",
        "drawer handle is forward aligned with the robot's gripper": "push drawer closed",
        "the robot's gripper is forward aligned with drawer handle": "push drawer closed",
    },
    "button-press-topdown": {
        "button is not vertically aligned with the robot's gripper": "put gripper above button",
        "the robot's gripper is not vertically aligned with button": "put gripper above button",
        "button is vertically aligned with the robot's gripper": "push down on button",
        "the robot's gripper is vertically aligned with button": "push down on button",
    },
    "peg-insert-side": {
        "peg is left of the robot's gripper": "put gripper above peg",
        "the robot's gripper is right of peg": "put gripper above peg",
        "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab peg",
        "peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg": "grab peg",
        "peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole": "align peg to hole",
        "peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg": "align peg to hole",
        "peg is horizontally aligned with hole": "insert peg into hole",
        "hole is horizontally aligned with peg": "insert peg into hole",
    },
    "window-open": {
        "window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle": "move gripper to right of window handle",
        "the robot's gripper is mostly below window handle and window handle is not vertically aligned with the robot's gripper": "move gripper to right of window handle",
        "window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper": "slide window left",
        "window handle is left of the robot's gripper and window handle is almost vertically aligned with the robot's gripper": "slide window left",
        "window handle is near the robot's gripper": "push window left harder",
        "window handle is around the robot's gripper": "push window left harder",
    },
    "window-close": {
        "window handle is not vertically aligned with the robot's gripper": "move gripper to left of window handle",
        "the robot's gripper is not vertically aligned with window handle": "move gripper to left of window handle",
        "window handle is right of the robot's gripper": "slide window right",
        "the robot's gripper is left of window handle": "slide window right",
        "window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper": "push window right harder",
        "window handle is vertically aligned with the robot's gripper and the robot's gripper is not left of window handle": "push window right harder",
    },
}

parsed_plans3 = {
    "reach": {"reach target is mostly below the robot's gripper": "reach to goal"},
    "push": {
        "puck is not behind target location and puck is not below the robot's gripper": "put the gripper above the puck",
        "puck is below the robot's gripper and puck is not near the robot's gripper": "push the gripper into the puck",
        "puck is near the robot's gripper and puck is below the robot's gripper": "slide the puck to the goal",
    },
    "pick-place": {
        "puck is not below the robot's gripper": "place gripper above puck",
        "puck is not below target location and puck is not near the robot's gripper": "drop gripper around puck",
        "puck is near the robot's gripper and gripper is open": "close gripper around puck",
        "gripper is closed": "place puck at goal",
    },
    "door-open": {
        "door handle is not almost vertically aligned with the robot's gripper": "put gripper above door handle",
        "door handle is not right of the robot's gripper and door handle is not forward aligned with the robot's gripper": "put gripper around door handle",
        "door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper": "push door closed",
    },
    "drawer-open": {
        "drawer handle is not vertically aligned with the robot's gripper": "put gripper above drawer handle",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "drawer handle is near the robot's gripper and drawer handle is not below the robot's gripper": "pull away from drawer",
    },
    "drawer-close": {
        "gripper is open": "put the gripper in front of the drawer",
        "drawer handle is below the robot's gripper and the robot's gripper is not mostly below drawer handle": "put the gripper above the drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper": "grab drawer handle",
        "drawer handle is forward aligned with the robot's gripper": "push drawer closed",
    },
    "button-press-topdown": {
        "button is not vertically aligned with the robot's gripper": "put gripper above button",
        "button is vertically aligned with the robot's gripper": "push down on button",
    },
    "peg-insert-side": {
        "peg is left of the robot's gripper": "put gripper above peg",
        "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab peg",
        "peg is forward aligned with the robot's gripper and the robot's gripper is not horizontally aligned with hole": "align peg to hole",
        "peg is horizontally aligned with hole": "insert peg into hole",
    },
    "window-open": {
        "window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle": "move gripper to right of window handle",
        "window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper": "slide window left",
        "window handle is near the robot's gripper": "push window left harder",
    },
    "window-close": {
        "window handle is not vertically aligned with the robot's gripper": "move gripper to left of window handle",
        "window handle is right of the robot's gripper": "slide window right",
        "window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper": "push window right harder",
    },
}

parsed_plans = {
    "reach": {
        "reach target is mostly below the robot's gripper": "reach to goal",
        "reach target is not right of the robot's gripper": "reach to goal",
    },
    "push": {
        "puck is not behind target location and puck is not below the robot's gripper": "put the gripper above the puck",
        "puck is not behind target location and the robot's gripper is not above puck": "put the gripper above the puck",
        "puck is below the robot's gripper and puck is not near the robot's gripper": "push the gripper into the puck",
        "puck is below the robot's gripper and the robot's gripper is not near puck": "push the gripper into the puck",
        "puck is near the robot's gripper and puck is below the robot's gripper": "slide the puck to the goal",
        "puck is near the robot's gripper and the robot's gripper is above puck": "slide the puck to the goal",
    },
    "pick-place": {
        "puck is not below the robot's gripper": "place gripper above puck",
        "the robot's gripper is not above puck": "place gripper above puck",
        "puck is not below target location and puck is not near the robot's gripper": "drop gripper around puck",
        "puck is not below target location and the robot's gripper is not near puck": "drop gripper around puck",
        "puck is near the robot's gripper and gripper is open": "close gripper around puck",
        "the robot's gripper is near puck and gripper is open": "close gripper around puck",
        "target location is forward aligned with the robot's gripper and puck is not touching the table": "place puck at goal",
        "the robot's gripper is forward aligned with target location and puck is not touching the table": "place puck at goal",
    },
    "door-open": {
        "door handle is not almost vertically aligned with the robot's gripper": "put gripper above door handle",
        "the robot's gripper is not almost vertically aligned with door handle": "put gripper above door handle",
        "door handle is not right of the robot's gripper and door handle is not forward aligned with the robot's gripper": "put gripper around door handle",
        "door handle is not right of the robot's gripper and the robot's gripper is not forward aligned with door handle": "put gripper around door handle",
        "door handle is forward aligned with the robot's gripper": "push door closed",
        "the robot's gripper is forward aligned with door handle": "push door closed",
    },
    "drawer-open": {
        "drawer handle is not vertically aligned with the robot's gripper": "put gripper above drawer handle",
        "the robot's gripper is not vertically aligned with drawer handle": "put gripper above drawer handle",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "drawer handle is near the robot's gripper and drawer handle is not below the robot's gripper": "pull away from drawer",
        "drawer handle is near the robot's gripper and the robot's gripper is not above drawer handle": "pull away from drawer",
    },
    "drawer-close": {
        "gripper is open": "put the gripper in front of the drawer",
        "drawer handle is vertically aligned with the robot's gripper and gripper is open": "put the gripper in front of the drawer",
        "drawer handle is below the robot's gripper and the robot's gripper is not mostly below drawer handle": "put the gripper above the drawer handle",
        "the robot's gripper is above drawer handle and the robot's gripper is not mostly below drawer handle": "put the gripper above the drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper": "grab drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with drawer handle": "grab drawer handle",
        "drawer handle is forward aligned with the robot's gripper": "push drawer closed",
        "the robot's gripper is forward aligned with drawer handle": "push drawer closed",
    },
    "button-press-topdown": {
        "button is not vertically aligned with the robot's gripper": "put gripper above button",
        "the robot's gripper is not vertically aligned with button": "put gripper above button",
        "button is vertically aligned with the robot's gripper": "push down on button",
        "the robot's gripper is vertically aligned with button": "push down on button",
    },
    "peg-insert-side": {
        "peg is left of the robot's gripper": "put gripper above peg",
        "the robot's gripper is right of peg": "put gripper above peg",
        "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab peg",
        "peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg": "grab peg",
        "peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole": "align peg to hole",
        "peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg": "align peg to hole",
        "peg is horizontally aligned with hole": "insert peg into hole",
        "hole is horizontally aligned with peg": "insert peg into hole",
    },
    "window-open": {
        "window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle": "move gripper to right of window handle",
        "the robot's gripper is mostly below window handle and window handle is not vertically aligned with the robot's gripper": "move gripper to right of window handle",
        "window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper": "slide window left",
        "window handle is left of the robot's gripper and window handle is almost vertically aligned with the robot's gripper": "slide window left",
        "window handle is near the robot's gripper": "push window left harder",
        "window handle is behind the robot's gripper": "push window left harder",
    },
    "window-close": {
        "window handle is not vertically aligned with the robot's gripper": "move gripper to left of window handle",
        "the robot's gripper is not vertically aligned with window handle": "move gripper to left of window handle",
        "window handle is right of the robot's gripper": "slide window right",
        "the robot's gripper is left of window handle": "slide window right",
        "window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper": "push window right harder",
        "window handle is vertically aligned with the robot's gripper and the robot's gripper is not left of window handle": "push window right harder",
    },
}

jit_eval_conditions = jax.jit(generate_metaworld_scene_dataset.eval_conditions,
static_argnames=["env_name", "conds", "fuzzy"])
# jit_eval_conditions = generate_metaworld_scene_dataset.eval_conditions


def embed_plan(plan):
    embedded_plan = {
        "conds": [embed_prompt.embed_condition(cond) for cond in plan["conds"]],
        "actions": [embed_prompt.embed_action(cond) for cond in plan["actions"]],
    }
    return embedded_plan


embedded_plans = {}
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
        # 'conds': self.param(f'{plan_name}.conds', lambda _: conds_embed),
        # 'actions': self.param(f'{plan_name}.actions', lambda _: actions_embed),
        "conds": conds_embed,
        "actions": actions_embed,
        "conds_str": conds,
        "actions_str": [plan[cond] for cond in conds],
    }
print("Done embedding plans")


class CondAgent(nn.Module):
    use_learned_evaluator: bool
    use_learned_controller: bool
    mix_in_language_space: bool
    plans: dict

    def setup(self):
        self.cond_evaluator = train_evaluator.ConditionEvaluator()
        self.learned_controller = LearnedController()

    def __call__(self, env_names, low_dim):
        info = {}
        plans = [self.plans[env_name] for env_name in env_names]
        if self.use_learned_evaluator:
            conds_padded, conds_mask = pad_list([plan["conds"] for plan in plans])
            conds_logits = self.cond_evaluator(low_dim, conds_padded)
            logits = 10 * jnp.tanh(conds_logits)
        else:
            true_values = []
            for (env_name, obs, plan) in zip(env_names, low_dim, plans):
                true_results = jit_eval_conditions(env_name, plan["conds_str"],
                                                   obs, fuzzy=True)
                true_values.append(true_results)
            padded_true_results, conds_mask = pad_list(true_values)
            logits = 10 * padded_true_results - 5
        controller_weights = nn.softmax(logits, axis=1, where=conds_mask, initial=0)
        info["logits"] = logits
        info["controller_weights"] = controller_weights
        controller_weights /= controller_weights.sum(axis=1)[0]
        controller_outputs = []
        if self.mix_in_language_space:
            assert self.use_learned_controller
            embedded_controller_names = [plan["actions"] for plan in plans]
            padded_controller_names, action_mask = pad_list(embedded_controller_names)
            action_embed = jnp.einsum(
                "ij,ijk->ik", controller_weights, padded_controller_names
            )
            actions, controller_info = self.learned_controller(low_dim, action_embed)
        else:
            if self.use_learned_controller:
                controller_outputs = []
                for (obs, plan) in zip(low_dim, plans):
                    action, controller_info = eslf.learned_controller(
                        jnp.array([obs for action_embed in plan["actions"]]),
                        plan["actions"],
                    )
                    controller_outputs.append(action)
                controller_outputs = jnp.array(controller_outputs)
                actions = jnp.einsum(
                    "ij,ijk->ik", controller_weights, controller_outputs
                )
            else:
                for (env_name, obs, plan) in zip(env_names, low_dim, plans):
                    parsed_obs = metaworld_jax_controllers.parse_obs(obs)
                    metaworld_controllers.np = jnp
                    controller_outputs.append(
                        [
                            metaworld_controllers.run_controller(name, parsed_obs)
                            for name in plan["actions_str"]
                        ]
                    )
                controller_outputs, _ = pad_list(controller_outputs)
                actions = jnp.einsum(
                    "ij,ijk->ik", controller_weights, controller_outputs
                )
        return actions, info

    def as_policy(self, env_name, state):
        return CondAgentPolicy(env_name=env_name, state=state, cond_agent=self)


class LearnedController(nn.Module):
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

    def __call__(self, low_dim, encoded_language_actions):
        info = {}
        reencoded_language = self.language_reencoder(encoded_language_actions)
        obs_and_lang_actions = jnp.concatenate([low_dim, reencoded_language], axis=-1)
        actions = self.action_model(obs_and_lang_actions)
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


def grouped_env_dataset(
    *,
    envs: str_list = MT50_ENV_NAMES,
    n_timesteps=1000,
    seed=jax_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
) -> [[dict]]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    with easy_process.Scope():
        workers = [
            sample_process(env_name=env_name, seed=seed, noise_scales=noise_scales)
            for env_name in envs
        ]
        datapoints = []
        successes = defaultdict(list)
        with tqdm(total=n_timesteps) as pbar:
            while len(datapoints) < n_timesteps:
                episode_block = []
                for (env_name, worker) in zip(envs, workers):
                    episode = worker.recv(block=True)
                    successes[env_name].append(episode_to_success(episode))
                    if shuffle_timesteps:
                        random.shuffle(episode)
                    episode_block.append(episode)
                new_datapoints = min(len(episode) for episode in episode_block)
                for i in range(new_datapoints):
                    datapoints.append([episode[i] for episode in episode_block])
                pbar.update(new_datapoints)
    for (env_name, success_rate) in successes.items():
        print(f"Data success rate for {env_name}:", np.mean(success_rate))
    return datapoints


@easy_process.subprocess_func
def sample_process(*, env_name: str, noise_scales: [float], seed: int, parent):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            ou_proc = OUProcess(dimensions=env.action_space.shape[0], sigma=noise_scale)
            episode = []
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
            parent.sendrecv(episode)


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


@easy_process.subprocess_func
def eval_process(*, env, policy, noise_scale: float, parent):
    while True:
        episode = []
        for data in sample_noisy_policy(env, policy, noise_scale):
            data["noise_scale"] = noise_scale
            episode.append(data)
        state_updates = parent.sendrecv(episode_to_success(episode))
        if state_updates:
            policy.state = policy.state.replace(params=state_updates[-1])
            parent.sendrecv("policy updated")

def episode_to_success(episode):
    success = False
    for data in episode:
        success |= data.get("success", 0) > 0
    return success

N_EVAL_WORKERS = 50

def evaluate_policy(env_name, n_episodes, env, policy, noise_scale):
    successes = []
    if n_episodes <= 10:
        for i in tqdm(range(n_episodes)):
            successes.append(episode_to_success(sample_noisy_policy(env, policy,
                                                                    noise_scale)))
    else:
        with easy_process.Scope():
            workers = [
                eval_process(env=env, policy=policy, noise_scale=noise_scale)
                for _ in range(N_EVAL_WORKERS)
            ]
            with tqdm(total=n_episodes) as pbar:
                while len(successes) < n_episodes:
                    for worker in workers:
                        success = worker.recv(block=False)
                        if success is not None and success != "policy updated":
                            successes.append(success)
                            pbar.update(1)
    print("Success rate for", env_name, ":", np.mean(successes))
    return np.mean(successes)


class EvalCallbacks(jax_utils.FitCallbacks):
    def __init__(self, seed, env_names, cond_agent, noise_scale=0.10):
        self.envs = {env_name: make_env(env_name, seed) for env_name in env_names}
        self.noise_scale = noise_scale
        self.cond_agent = cond_agent
        self.process_scope = easy_process.Scope()
        self.workers = {}
        self.n_episodes = 50
        self.step_period = 10
        self.current_step = 0

    def epoch_start(self, state):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete(state)
        else:
            return state, {}

    def training_complete(self, state):
        infos = {}
        for (env_name, env) in self.envs.items():
            policy = self.cond_agent.as_policy(env_name, state)
            if env_name in self.workers:
                workers = self.workers[env_name]
                for worker in workers:
                    worker.send(state.params, block=True)
                for worker in workers:
                    msg = None
                    while msg != "policy updated":
                        msg = worker.recv(block=True)
            else:
                easy_process.SCOPE_STACK.append(self.process_scope)
                workers = [eval_process(env=env, policy=policy, noise_scale=self.noise_scale)
                           for _ in range(N_EVAL_WORKERS)]
                self.workers[env_name] = workers
                easy_process.SCOPE_STACK.pop()

            successes = []
            with tqdm(total=self.n_episodes) as pbar:
                while len(successes) < self.n_episodes:
                    for worker in workers:
                        success = worker.recv(block=False)
                        if success is not None and success != "policy updated":
                            successes.append(success)
                            pbar.update(1)
            print(f"Success rate for {env_name}:", np.mean(successes))
            infos[f"{env_name}/SuccessRate"] = np.mean(successes)
        return state, infos



def train_and_evaluate(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    test_envs: str_list = MT10_ENV_NAMES,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    batch_size=4,
    noise_scale=0.1,
):

    data = grouped_env_dataset(envs=train_envs, n_timesteps=n_timesteps, seed=seed)
    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=True,
        use_learned_controller=True,
        plans=embedded_plans,
    )
    callbacks = EvalCallbacks(seed, train_envs + test_envs, cond_agent)
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
    print('Done saving cache')
    callbacks.process_scope.close()

    # workdir = os.path.expanduser(
    # f"~/data/cond_agent_seed={seed}_noise-scale={noise_scale}"
    # )
    # rng = jax.random.PRNGKey(seed)
    # summary_writer = tensorboard.SummaryWriter(workdir)
    # summary_writer.hparams(dict(locals()))

    # train_env_names = [name for name in train_envs.split(",") if name]
    # test_env_names = [name for name in test_envs.split(",") if name]
    # max_episode_length = 500
    # max_size = len(train_env_names) * max_episode_length * 10

    # rng, init_rng = jax.random.split(rng)
    # learning_rate = 1e-4
    # momentum = 0.99
    # cond_agent = CondAgent()
    # params = cond_agent.init(
    # rng,
    # ["drawer-close", "pick-place"] * int(batch_size / 2),
    # jnp.ones([batch_size, 39]),
    # jnp.ones(
    # [
    # batch_size,
    # np.max(
    # [
    # len(embedded_plans[env_name]["conds"])
    # for env_name in ["drawer-close", "pick-place"]
    # ]
    # ),
    # ]
    # ),
    # )
    # params = params.copy({"params": {"cond_evaluator": load_best_evaluator_params()}})
    # tx = optax.sgd(learning_rate, momentum)
    # state = train_state.TrainState.create(
    # apply_fn=cond_agent.apply, params=params, tx=tx
    # )
    # for env_name in train_env_names + test_env_names:
    # env = make_env(env_name, seed)
    # policy = cond_agent.as_policy(env_name, state)
    # success = evaluate_policy(
    # env_name, 10, lambda: sample_noisy_policy(env, policy, 0.10)
    # )


if __name__ == "__main__":
    clize.run(train_and_evaluate)
