import collections
from collections import defaultdict
from dataclasses import dataclass
import clize
from functools import partial
import os
import typing

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

# {
# "button-press-topdown": {
# "button is not vertically aligned with the robot's gripper": "put "
# "gripper "
# "above "
# "button",
# "button is vertically aligned with the robot's gripper": "push "
# "down "
# "on "
# "button",
# },
# "door-open": {
# "door handle is left of the robot's gripper and gripper is closed": "put "
# "gripper "
# "around "
# "door "
# "handle",
# "door handle is not almost vertically aligned with the robot's gripper": "put "
# "gripper "
# "above "
# "door "
# "handle",
# "door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper": "push "
# "door "
# "closed",
# },
# "drawer-close": {
# "drawer handle is below the robot's gripper": "put the "
# "gripper above "
# "the drawer "
# "handle",
# "drawer handle is forward aligned with the robot's gripper": "push "
# "drawer "
# "closed",
# "drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper": "grab "
# "drawer "
# "handle",
# "gripper is open": "put the gripper in front of the drawer",
# },
# "drawer-open": {
# "drawer handle is not vertically aligned with the robot's gripper": "put "
# "gripper "
# "above "
# "drawer "
# "handle",
# "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle": "put "
# "gripper "
# "around "
# "drawer "
# "handle",
# "the robot's gripper is around drawer handle": "pull away " "from drawer",
# },
# "peg-insert-side": {
# "peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole": "align "
# "peg "
# "to "
# "hole",
# "peg is horizontally aligned with hole": "insert peg into " "hole",
# "peg is left of the robot's gripper": "put gripper above " "peg",
# "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab "
# "peg",
# },
# "pick-place": {
# "gripper is closed": "place puck at goal",
# "puck is around the robot's gripper and gripper is open": "close "
# "gripper "
# "around "
# "puck",
# "puck is below the robot's gripper and puck is not around the robot's gripper": "drop "
# "gripper "
# "around "
# "puck",
# "puck is not below the robot's gripper": "place gripper above " "puck",
# },
# "push": {
# "puck is below the robot's gripper and puck is not near the robot's gripper": "push "
# "the "
# "gripper "
# "into "
# "the "
# "puck",
# "puck is near the robot's gripper": "slide the puck to the goal",
# "puck is not below the robot's gripper": "put the gripper above the " "puck",
# },
# "reach": {"reach target is mostly below the robot's gripper": "reach to goal"},
# "window-close": {
# "window handle is not vertically aligned with the robot's gripper": "move "
# "gripper "
# "to "
# "left "
# "of "
# "window "
# "handle",
# "window handle is right of the robot's gripper": "slide " "window " "right",
# "window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper": "push "
# "window "
# "right "
# "harder",
# },
# "window-open": {
# "window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper": "slide "
# "window "
# "left",
# "window handle is near the robot's gripper": "push window " "left harder",
# "window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle": "move "
# "gripper "
# "to "
# "right "
# "of "
# "window "
# "handle",
# },
# }


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
    def setup(self):
        self.plans = embedded_plans
        self.cond_evaluator = train_evaluator.ConditionEvaluator()

    def __call__(self, env_names, low_dim, true_cond_results):
        info = {}
        plans = [self.plans[env_name] for env_name in env_names]
        conds_padded, conds_mask = pad_list([plan["conds"] for plan in plans])
        conds_logits = self.cond_evaluator(low_dim, conds_padded)
        true_logits = 10 * true_cond_results - 5
        # logits = 2 * (0.9 * conds_logits + 0.1 * true_logits)
        logits = 0.2 * (10 * jnp.tanh(conds_logits)) + 0.8 * true_logits
        controller_weights = nn.softmax(2 * logits, axis=1,
        where=conds_mask,
        initial=0)
        # controller_weights = controller_weights * (1.0 + true_cond_results)
        info["logits"] = logits
        info["truth_values"] = conds_logits
        info["controller_weights"] = controller_weights
        info["true_cond_results"] = true_cond_results
        info["weight_correlation"] = (
            controller_weights * true_cond_results - 0.5 * conds_mask
        )
        # perfect_weights = []
        controller_weights /= controller_weights.sum(axis=1)[0]
        controller_outputs = []
        for (env_name, obs, plan) in zip(env_names, low_dim, plans):
            # descriptors = generate_metaworld_scene_dataset.describe_obs(env_name,
            # np.array(obs))
            # perfect_weights.append([
            # jnp.array(descriptors[cond]) for cond in plan['conds_str']
            # ])
            parsed_obs = metaworld_jax_controllers.parse_obs(obs)
            metaworld_controllers.np = jnp
            controller_outputs.append(
                [
                    metaworld_controllers.run_controller(name, parsed_obs)
                    for name in plan["actions_str"]
                ]
            )
        controller_outputs, _ = pad_list(controller_outputs)
        weighted_outputs = jnp.einsum(
            "ij,ijk->ik", controller_weights, controller_outputs
        )
        return weighted_outputs, info

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
        plans = [embedded_plans[env_name] for env_name in env_names]
        perfect_weights = []
        for (env_name, obs, plan) in zip(env_names, observations, plans):
            descriptors = generate_metaworld_scene_dataset.describe_obs(
                env_name, np.array(obs)
            )
            perfect_weights.append(
                [jnp.array(descriptors[cond]) for cond in plan["conds_str"]]
            )
        true_cond_results, _ = pad_list(perfect_weights)

        action, info = run_cond_agent(
            self.state, tuple(env_names), observations, true_cond_results
        )

        # for (k, v) in info.items():
          # print(k, v)

        return np.asarray(action), info


@partial(jax.jit, static_argnames=["env_names"])
def run_cond_agent(state, env_names, observations, true_cond_results):
    return state.apply_fn(state.params, env_names, observations, true_cond_results)


@jax.jit
def update_model(state, grads):
    return state.apply_gradients(grads=grads)


# @partial(jax.jit, static_argnames=['env_names'])
def apply_model(state, env_names, observations, action_targets):
    def loss_fn(params):
        action = state.apply_fn(params, env_names, observations)
        loss = jnp.mean(optax.l2_loss(action, action_targets))
        return loss

    grad_fn = jax.value_and_grad(loss_fn)
    loss, grads = grad_fn(state.params)
    return grads, loss


def train_epoch(state, batch):
    observations = []
    action_targets = []
    env_names = []
    for sample_pkl in batch:
        sample = pickle.loads(sample_pkl[0].data[0].item())
        observations.append(sample["observation"])
        action_targets.append(sample["action"])
        env_names.append(sample["env_name"])
    obs_batch = np.stack(observations)
    action_batch = np.stack(action_targets)
    grads, loss = apply_model(state, tuple(env_names), obs_batch, action_batch)
    state = update_model(state, grads)
    return state, loss


@easy_process.subprocess_func
def sampler_proc(env_name, port, seed, noise_scale, *, parent):
    client = reverb.Client(f"localhost:{port}")

    while True:
        print("waiting")
        msg = parent.recv()
        if msg == "stop":
            return
        elif msg == "gather":
            try:
                env = get_env(env_name, seed)
                max_episode_length = 500
                policy = SawyerUniversalV2Policy(env_name=env_name)
                observation = env.reset()
                use_random = False
                for i in tqdm(range(max_episode_length)):
                    print(i)
                    action = policy.get_action(observation)
                    action_noisy = action + np.random.normal(scale=noise_scale)
                    observation, reward, done, info = env.step(action_noisy)
                    store(env_name, client, observation, action, reward)
                return_env(env_name, env)
            except Exception as ex:
                print(ex)
            parent.send("gather done")
        else:
            raise TypeError("Unknown message")


def eval_policy(policy, env_names, seed):
    env_names = tuple(env_names)
    envs = [get_env(name, seed) for name in env_names]

    max_episode_length = 500
    observations = [env.reset() for env in envs]
    use_random = False
    rewards = {name: [] for name in env_names}
    for i in tqdm(range(max_episode_length)):
        actions = step_agent(policy.state, env_names, jnp.array(observations))
        for i, action in enumerate(actions):
            observations[i], reward, done, info = envs[i].step(np.array(action))
            rewards[env_names[i]].append(reward)

    for (env_name, env) in zip(env_names, envs):
        return_env(env_name, env)
    return rewards


def load_best_evaluator_params():
    with open(os.path.expanduser("~/data/best_evaluator.pkl"), "rb") as f:
        cond_eval_state = pickle.load(f)
    return cond_eval_state["params"]


def evaluate_policy(env_name, n_episodes, episode_factory):
    successes = []
    for i in tqdm(range(n_episodes)):
        success = False
        for data in episode_factory():
            success |= data.get("success", 0) > 0
        successes.append(success)
    print("Success rate for", env_name, ":", np.mean(successes))
    return np.mean(successes)


def train_and_evaluate(
    *,
    train_envs=",".join([e[:-3] for e in MT10_V2.keys()]),
    test_envs="",
    # test_envs=','.join([e[:-3] for e in MT10_V2.keys()]),
    seed=random.randrange(1000),
    num_batches=1e6,
    batch_size=16,
    noise_scale=0.1,
):
    workdir = os.path.expanduser(
        f"~/data/cond_agent_seed={seed}_noise-scale={noise_scale}"
    )
    rng = jax.random.PRNGKey(seed)
    summary_writer = tensorboard.SummaryWriter(workdir)
    summary_writer.hparams(dict(locals()))

    train_env_names = [name for name in train_envs.split(",") if name]
    test_env_names = [name for name in test_envs.split(",") if name]
    max_episode_length = 500
    max_size = len(train_env_names) * max_episode_length * 10

    rng, init_rng = jax.random.split(rng)
    learning_rate = 1e-4
    momentum = 0.99
    cond_agent = CondAgent()
    params = cond_agent.init(
        rng,
        ["drawer-close", "pick-place"] * int(batch_size / 2),
        jnp.ones([batch_size, 39]),
        jnp.ones([batch_size, np.max([len(embedded_plans[env_name]['conds'])
                                      for env_name in ['drawer-close', 'pick-place']])]),
    )
    params = params.copy({"params": {"cond_evaluator": load_best_evaluator_params()}})
    tx = optax.sgd(learning_rate, momentum)
    state = train_state.TrainState.create(
        apply_fn=cond_agent.apply, params=params, tx=tx
    )
    for env_name in train_env_names + test_env_names:
        env = make_env(env_name, seed)
        policy = cond_agent.as_policy(env_name, state)
        success = evaluate_policy(
            env_name, 10, lambda: sample_noisy_policy(env, policy, 0.10)
        )


if __name__ == "__main__":
    clize.run(train_and_evaluate)
