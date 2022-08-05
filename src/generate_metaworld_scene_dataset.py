import shutil as sh
from collections import defaultdict
from pprint import pprint
from dataclasses import dataclass
from functools import partial
import random
import os
import pickle
import typing
import difflib

import jax
import numpy as np
import jax.numpy as jnp

import clize
from tqdm import tqdm

import easy_process
from metaworld.envs.mujoco.env_dict import MT10_V2
import metaworld_controllers
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs, run_controller
import metaworld_universal_policy
from sample_utils import (
    make_env,
    sample_noisy_policy,
    sample_policy_with_noise_process,
    collect_noisy_episodes,
)
from run_utils import float_list, str_list
from sample_utils import MT50_ENV_NAMES
from ou_process import OUProcess
import jax_utils

import ou_process


class FixedDict(dict):
    def __setitem__(self, key, value):
        assert key in self, f"{key} not present in dict"
        return super().__setitem__(key, value)


COORDINATE_RELATIONS = [
    "near",
    "around",
    "left of",
    "right of",
    "behind",
    "in front of",
    "above",
    "below",
    "vertically aligned with",
    "almost vertically aligned with",
    "mostly below",
    "horizontally aligned with",
    "forward aligned with",
]


def describe_relative_coordinates(xyz1, xyz2):
    descriptors = FixedDict({relation: 0 for relation in COORDINATE_RELATIONS})
    if np.linalg.norm(xyz1 - xyz2) < 0.04:
        descriptors["near"] = 1.0
    if np.linalg.norm(xyz1 - xyz2 + [0, 0, 0.02]) < 0.03:
        descriptors["around"] = 1.0
    if xyz1[0] - xyz2[0] > 0.04:
        descriptors["left of"] = 1.0
    if xyz1[0] - xyz2[0] < -0.04:
        descriptors["right of"] = 1.0
    if xyz1[1] - xyz2[1] > 0.04 and np.linalg.norm(xyz1[[0, 2]] - xyz2[[0, 2]]) < 0.04:
        descriptors["behind"] = 1.0
    if xyz1[1] - xyz2[1] < -0.04 and np.linalg.norm(xyz1[[0, 2]] - xyz2[[0, 2]]) < 0.04:
        descriptors["in front of"] = 1.0
    if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] > 0.0:
        descriptors["above"] = 1.0
    if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02 and xyz1[2] - xyz2[2] < 0:
        descriptors["below"] = 1.0
    if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.06:
        descriptors["vertically aligned with"] = 1.0
    if np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.12:
        descriptors["almost vertically aligned with"] = 1.0
    if xyz1[2] < xyz2[2] + 0.23:
        descriptors["mostly below"] = 1.0
    if np.linalg.norm(xyz1[1:] - xyz2[1:]) < 0.03:
        descriptors["horizontally aligned with"] = 1.0
    if np.linalg.norm(xyz1[[0, 2]] - xyz2[[0, 2]]) < 0.03:
        descriptors["forward aligned with"] = 1.0
    descriptors = dict(descriptors)
    for key in list(descriptors.keys()):
        descriptors[f"not {key}"] = 1 - descriptors[key]
    return descriptors


OBJECT_NAMES = {
    "drawer-open": {
        "obj1_pos": "drawer handle",
    },
    "drawer-close": {
        "obj1_pos": "drawer handle",
    },
    "peg-insert-side": {
        "obj1_pos": "peg",
        # The goal is weirdly offset, so it's hacked in below
    },
    "reach": {"goal_pos": "reach target"},
    "window-open": {
        "obj1_pos": "window handle",
    },
    "window-close": {
        "obj1_pos": "window handle",
    },
    "door-open": {"obj1_pos": "door handle"},
    "push": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "pick-place": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "button-press-topdown": {
        "obj1_pos": "button",
    },
    "sweep": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
    "assembly": {
        "obj1_pos": "wrench",
        "goal_pos": "peg",
    },
    "basketball": {
        "obj1_pos": "ball",
        "goal_pos": "hoop",
    },
    "bin-picking": {
        "obj1_pos": "cube",
    },
    "box-close": {
        "obj1_pos": "lid",
        "goal_pos": "box",
    },
    "button-press-topdown-wall": {
        "obj1_pos": "button",
    },
    "button-press": {
        "obj1_pos": "button",
    },
    "button-press-wall": {
        "obj1_pos": "button",
    },
    "coffee-button": {
        "obj1_pos": "button",
    },
    "coffee-pull": {
        "obj1_pos": "mug",
        "goal_pos": "target location",
    },
    "coffee-push": {
        "obj1_pos": "mug",
        "goal_pos": "target location",
    },
    "dial-turn": {
        "obj1_pos": "dial",
    },
    "disassemble": {
        "obj1_pos": "wrench",
        "goal_pos": "peg",
    },
    "door-close": {
        "obj1_pos": "door",
        "goal_pos": "target location",
    },
    "door-lock": {
        "obj1_pos": "door's lock",
    },
    "door-unlock": {
        "obj1_pos": "door's lock",
    },
    "faucet-close": {
        "obj1_pos": "faucet",
    },
    "faucet-open": {
        "obj1_pos": "faucet",
    },
    "hammer": {
        "obj1_pos": "hammer",
    },
    "hand-insert": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "handle-press-side": {
        "obj1_pos": "handle",
    },
    "handle-press": {
        "obj1_pos": "handle",
    },
    "handle-pull-side": {
        "obj1_pos": "handle",
    },
    "handle-pull": {
        "obj1_pos": "handle",
    },
    "lever-pull": {
        "obj1_pos": "lever",
    },
    "peg-unplug-side": {
        "obj1_pos": "peg",
    },
    "pick-out-of-hole": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "pick-place-wall": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "plate-slide-back-side": {
        "obj1_pos": "plate",
    },
    "plate-slide-back": {
        "obj1_pos": "plate",
    },
    "plate-slide-side": {
        "obj1_pos": "plate",
    },
    "plate-slide": {
        "obj1_pos": "plate",
        "goal_pos": "target location",
    },
    "push-back": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "push-wall": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "reach-wall": {
        "goal_pos": "target location",
    },
    "shelf-place": {
        "obj1_pos": "block",
        "goal_pos": "shelf",
    },
    "soccer": {
        "obj1_pos": "ball",
        "goal_pos": "goal",
    },
    "stick-pull": {
        "obj1_pos": "stick",
        "obj2_pos": "thermos",
        "goal_pos": "target location",
    },
    "stick-push": {
        "obj1_pos": "stick",
        "obj2_pos": "thermos",
        "goal_pos": "target location",
    },
    "sweep-into": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
    "sweep": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
}

OBJECT_NAMES_TO_PARSE_NAME = {
    env_name: {v: k for (k, v) in env_map.items()}
    for (env_name, env_map) in OBJECT_NAMES.items()
}

assert len(OBJECT_NAMES) == 50
assert set(OBJECT_NAMES.keys()) == set(MT50_ENV_NAMES)

WALL_ENVS = {
    "reach-wall",
    "pick-place-wall",
    "push-wall",
    "button-press-wall",
    "button-press-topdown-wall",
}

MT50_TASK_DESCRIPTIONS = {
    "door-open": "Open the door",
    "drawer-open": "open the drawer",
    "assembly": "put the wrench around the peg",
    "basketball": "put the ball into into the hoop",
    "button-press-topdown": "push the button down from above",
    "button-press-topdown-wall": "push the button down from above with a short wall in the way",
    "button-press": "push the button from the front",
    "button-press-wall": "push the button from the front with a short wall in the way",
    "coffee-button": "push the button on the coffee machine",
    "coffee-pull": "grab the mug and pull it to the target location",
    "coffee-push": "grab the mug and move it to the target location",
    "bin-picking": "pick up the cube and place it in the target bin",
    "dial-turn": "turn the dial",
    "disassemble": "pull the wrench off the peg",
    "door-open": "pull the door open",
    "drawer-close": "push the drawer close",
    "drawer-open": "pull the drawer open",
    "faucet-open": "turn the faucet left",
    "faucet-close": "turn the faucet right",
    "hammer": "hit the nail with the hammer",
    "box-close": "pick up the box lid and place it on the box",
    "handle-press-side": "push down the handle from the side",
    "handle-press": "push down the handle",
    "handle-pull-side": "pull up the handle from the side",
    "handle-pull": "pull up the handle",
    "lever-pull": "rotate the lever up",
    "peg-insert-side": "insert the peg into the hole from the side",
    "peg-unplug-side": "pull the peg out from the side",
    "pick-out-of-hole": "pick up the peg out of the hole and hold it at the target location",
    "pick-place": "pick up the puck and hold it at the target location",
    "door-lock": "turn the dial on the door",
    "pick-place-wall": "pick up the puck and hold it at the target location with a short wall in the way",
    "plate-slide": "slide the plate into the target location",
    "plate-slide-side": "slide the plate sideways into the target location",
    "plate-slide-back": "slide the plate back into the target location",
    "plate-slide-back-side": "slide the plate back sideways into the target location",
    "push-back": "grab the puck and move it back to the target location",
    "push": "grab the puck and move it to the target location",
    "push-wall": "grab the puck and move it to the target location with a small wall in the way",
    "reach": "reach to the target location",
    "door-unlock": "turn the dial on the door",
    "reach-wall": "reach to the target location with a short wall in the way",
    "shelf-place": "pick up the block and place it at the target location",
    "soccer": "push the soccer ball into the target location",
    "stick-push": "use the stick to push the thermos to the target location",
    "stick-pull": "use the stick to pull the thermos to the target location",
    "sweep-into": "grab the cube and move it to the target location",
    "sweep": "grab the cube and move sideways it to the target location",
    "window-open": "Slide the window open",
    "window-close": "Slide the window closed",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}

assert set(MT50_TASK_DESCRIPTIONS.keys()) == set(MT50_ENV_NAMES)
assert len(MT50_TASK_DESCRIPTIONS) == 50

MT10_PLANS = {
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
        "puck is below the robot's gripper and gripper is open": "drop gripper around puck",
        "the robot's gripper is above puck and gripper is open": "drop gripper around puck",
        "puck is near the robot's gripper and gripper is open": "close gripper around puck",
        "the robot's gripper is near puck and gripper is open": "close gripper around puck",
        "puck is below the robot's gripper and gripper is closed": "place puck at goal",
        "the robot's gripper is above puck and gripper is closed": "place puck at goal",
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


def describe_obs(env_name, obs):
    if not isinstance(obs, dict):
        obs = parse_obs(obs)
    keys_to_names = {"hand_pos": "the robot's gripper"}
    keys_to_names.update(OBJECT_NAMES[env_name])
    descriptors = {}
    object_locations = []
    for (key, name) in OBJECT_NAMES[env_name].items():
        object_locations.append((name, obs[key]))
    object_locations.append(("the robot's gripper", obs["hand_pos"]))
    if env_name == "peg-insert-side":
        object_locations.append(("hole", np.array([-0.35, obs["goal_pos"][1], 0.16])))
    elif (
        env_name == "reach-wall"
        or env_name == "push-wall"
        or env_name == "pick-place-wall"
    ):
        # TODO(zentner): Maybe sure the wall coordinates reflect the center of the
        # wall.
        object_locations.append(("wall", np.array([0.1, 0.75, 0.06])))
    elif env_name == "button-press-wall":
        object_locations.append(("wall", np.array([0.1, 0.6, 0.0])))
    elif env_name == "button-press-topdown-wall":
        object_locations.append(("wall", np.array([0.1, 0.7, 0.0])))
    for (i, (name1, xyz1)) in enumerate(object_locations):
        for (j, (name2, xyz2)) in enumerate(object_locations):
            if name1 == name2:
                continue
            disc = describe_relative_coordinates(xyz1, xyz2)
            for (key, val) in disc.items():
                if (
                    key == "around" or key == "not around"
                ) and name1 != "the robot's gripper":
                    continue
                descriptors[f"{name1} is {key} {name2}"] = val
    for (key, name) in OBJECT_NAMES[env_name].items():
        if key == "goal_pos":
            continue
        gripper_motion = obs["hand_pos"] - obs["last_hand_pos"]
        obj_motion = obs[key] - obs[f"last_{key}"]

        if obs[key][2] > 0.02:
            descriptors[f"{name} is touching the table"] = 0.0
            descriptors[f"{name} is not touching the table"] = 1.0
        else:
            descriptors[f"{name} is touching the table"] = 1.0
            descriptors[f"{name} is not touching the table"] = 0.0

    if obs["gripper_distance_apart"] > 0.75:
        descriptors["gripper is open"] = 1.0
        descriptors["gripper is closed"] = 0.0
    else:
        descriptors["gripper is open"] = 0.0
        descriptors["gripper is closed"] = 1.0

    # for (key, value) in descriptors.items():
    # if value > 0:
    # print(key)
    conjunction_descriptors = {}
    for (desc1, value1) in descriptors.items():
        for (desc2, value2) in descriptors.items():
            conjunction_descriptors[f"{desc1} and {desc2}"] = value1 * value2
    descriptors.update(conjunction_descriptors)
    # descriptors_enumerated = enumerate_descriptors(env_name)
    # # pprint(descriptors_enumerated)
    # assert set(descriptors_enumerated) == set(descriptors.keys())
    # values = eval_conditions(env_name, tuple(descriptors_enumerated), obs)
    # for (cond, val) in zip(descriptors_enumerated, values):
    # # for cond in descriptors_enumerated:
    # # val = eval_conditions(env_name, [cond], obs)[0]
    # if bool(descriptors[cond]) != val:
    # print(f'now: {cond!r} = {val}')
    # print(f'old: {descriptors[cond]}')
    # assert bool(descriptors[cond]) == val, f"Evaluation doesn't match for {cond!r}"
    return descriptors


POSITIVE_RELATION_SUBSTR = [f" is {rel} " for rel in COORDINATE_RELATIONS]
NEGATIVE_RELATION_SUBSTR = [f" is not {rel} " for rel in COORDINATE_RELATIONS]

WALL_ENVS = {
    "reach-wall",
    "push-wall",
    "pick-place-wall",
    "button-press-wall",
    "button-press-topdown-wall",
}

@partial(jax.jit, static_argnames=["env_name", "object_name", "fuzzy"])
def get_object_location(env_name: str, object_name: str, obs, fuzzy: bool=False):
    try:
        parse_name = OBJECT_NAMES_TO_PARSE_NAME[env_name][object_name]
    except KeyError as exc:
        if object_name == "the robot's gripper":
            parse_name = "hand_pos"
        elif object_name.startswith('the '):
            return get_object_location(env_name, object_name.split('the ')[1],
                                       obs, fuzzy=fuzzy)
        elif env_name == "peg-insert-side" and object_name == "hole":
            return jnp.array([-0.35, obs["goal_pos"][1], 0.16])
        elif env_name in WALL_ENVS and object_name == "wall":
            if (
                env_name == "reach-wall"
                or env_name == "push-wall"
                or env_name == "pick-place-wall"
            ):
                # TODO(zentner): Maybe sure the wall coordinates reflect the center of the
                # wall.
                return jnp.array([0.1, 0.75, 0.06])
            elif env_name == "button-press-wall":
                return jnp.array([0.1, 0.6, 0.0])
            elif env_name == "button-press-topdown-wall":
                return jnp.array([0.1, 0.7, 0.0])
        elif fuzzy:
            object_names = list(OBJECT_NAMES_TO_PARSE_NAME[env_name].keys())
            matches = sorted(object_names,
                             key=lambda name: difflib.SequenceMatcher(None, name, object_name).ratio(),
                             reverse=True)
            parse_name = OBJECT_NAMES_TO_PARSE_NAME[env_name][matches[0]]
        else:
            raise exc
    # print(f'{object_name!r} (a.k.a. {parse_name!r}) is located at {obs[parse_name]}')
    return obs[parse_name]


# @partial(jax.jit, static_argnames=["rel"])
def eval_relation(rel: str, xyz1: np.ndarray, xyz2: np.ndarray) -> bool:
    assert rel.strip() == rel
    if rel == "near":
        return jnp.linalg.norm(xyz1 - xyz2) < 0.04
    elif rel == "around":
        return jnp.linalg.norm(xyz1 - xyz2 + jnp.array([0, 0, 0.02])) < 0.03
    elif rel == "left of":
        return xyz1[0] - xyz2[0] > 0.04
    elif rel == "right of":
        return xyz1[0] - xyz2[0] < -0.04
    elif rel == "behind":
        return (xyz1[1] - xyz2[1] > 0.04) * (
            jnp.linalg.norm(jnp.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "in front of":
        return (xyz1[1] - xyz2[1] < -0.04) * (
            jnp.linalg.norm(jnp.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "above":
        return (jnp.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] > 0.0)
    elif rel == "below":
        return (jnp.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] < 0)
    elif rel == "vertically aligned with":
        return jnp.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.06
    elif rel == "almost vertically aligned with":
        return jnp.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.12
    elif rel == "mostly below":
        return xyz1[2] < xyz2[2] + 0.23
    elif rel == "horizontally aligned with":
        return jnp.linalg.norm(xyz1[1:] - xyz2[1:]) < 0.03
    elif rel == "forward aligned with":
        return jnp.linalg.norm(jnp.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.03
    else:
        raise TypeError(f"Unknown coordinate relation {rel}")


# @partial(jax.jit, static_argnames=["env_name", "conds"])
def eval_conditions(env_name: str, conds: typing.Tuple[str], obs, fuzzy=False):
    if not isinstance(obs, dict):
        obs = parse_obs(obs)
    results = []
    for full_cond in conds:
        base_conds = full_cond.split(" and ")

        base_results = []
        for cond in base_conds:
            if cond == "gripper is open":
                base_results.append(obs["gripper_distance_apart"] > 0.75)
            elif cond == "gripper is closed":
                base_results.append(obs["gripper_distance_apart"] <= 0.75)
            elif cond.endswith(" is not touching the table"):
                object_name = cond.split(" is not touching the table")[0]
                xyz = get_object_location(env_name, object_name, obs, fuzzy)
                base_results.append(xyz[2] > 0.02)
            elif cond.endswith(" is touching the table"):
                object_name = cond.split(" is touching the table")[0]
                xyz = get_object_location(env_name, object_name, obs, fuzzy)
                base_results.append(xyz[2] <= 0.02)
            elif any(substr in cond for substr in NEGATIVE_RELATION_SUBSTR):
                neg_relations = [
                    rel for rel in COORDINATE_RELATIONS if f" is not {rel} " in cond
                ]
                assert len(neg_relations) >= 1
                rel = neg_relations[0]
                obj_name1, obj_name2 = cond.split(f" is not {rel} ")
                xyz1 = get_object_location(env_name, obj_name1, obs, fuzzy)
                xyz2 = get_object_location(env_name, obj_name2, obs, fuzzy)
                base_results.append(1 - eval_relation(rel, xyz1, xyz2))
            elif any(substr in cond for substr in POSITIVE_RELATION_SUBSTR):
                pos_relations = [
                    rel for rel in COORDINATE_RELATIONS if f" is {rel} " in cond
                ]
                assert len(pos_relations) >= 1
                rel = pos_relations[0]
                obj_name1, obj_name2 = cond.split(f" is {rel} ")
                xyz1 = get_object_location(env_name, obj_name1, obs, fuzzy)
                xyz2 = get_object_location(env_name, obj_name2, obs, fuzzy)
                base_results.append(eval_relation(rel, xyz1, xyz2))
            elif fuzzy:
                possible_conditions = enumerate_descriptors(env_name)
                matches = sorted(possible_conditions,
                             key=lambda a: difflib.SequenceMatcher(None, a, cond).ratio(),
                             reverse=True)
            else:
                raise TypeError(f"Could not eval condition {cond}")
        results.append(jnp.all(jnp.array(base_results)))
    return jnp.array(results)


def enumerate_descriptors(env_name: str) -> [str]:
    object_names = ["the robot's gripper"] + list(OBJECT_NAMES[env_name].values())
    if env_name == "peg-insert-side":
        object_names.append("hole")
    elif (
        env_name == "reach-wall"
        or env_name == "push-wall"
        or env_name == "pick-place-wall"
        or env_name == "button-press-wall"
        or env_name == "button-press-topdown-wall"
    ):
        object_names.append("wall")
    descriptors = []
    for name1 in object_names:
        for name2 in object_names:
            if name1 == name2:
                continue
            for rel in COORDINATE_RELATIONS:
                if rel == "around" and name1 != "the robot's gripper":
                    continue
                descriptors.append(f"{name1} is {rel} {name2}")
                descriptors.append(f"{name1} is not {rel} {name2}")
    for (key, name) in OBJECT_NAMES[env_name].items():
        if key == "goal_pos":
            continue
        descriptors.append(f"{name} is touching the table")
        descriptors.append(f"{name} is not touching the table")

    descriptors.append("gripper is open")
    descriptors.append("gripper is closed")

    conjunction_descriptors = []
    for desc1 in descriptors:
        for desc2 in descriptors:
            conjunction_descriptors.append(f"{desc1} and {desc2}")
    all_descriptors = descriptors + conjunction_descriptors
    return all_descriptors


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


def controller_names_for_env(env_name):
    for (controller_name, controller) in metaworld_controllers.CONTROLLERS.items():
        if controller["env-name"] == env_name:
            yield controller_name


@dataclass
class DescriptorPolicy:
    descriptor_to_controller: dict
    env_name: str
    controller_choice_prob: float = 1.0
    base_weight: float or None = None

    def get_action(self, observation):
        tree = metaworld_controllers.DECISION_TREES[self.env_name]["function"]
        obs = parse_obs(observation)
        descriptions = describe_obs(self.env_name, obs)
        candidate_controllers = [
            con
            for (desc, con) in self.descriptor_to_controller.items()
            if descriptions[desc] > 0
        ]
        if candidate_controllers and np.random.uniform() < self.controller_choice_prob:
            controller_name = random.choice(candidate_controllers)
        else:
            controller_name = random.choice(
                list(self.descriptor_to_controller.values())
            )
        ground_truth_controller_name = tree(obs)
        info = {}
        info["controller_name"] = controller_name
        info["candidate_controllers"] = list(set(candidate_controllers))
        if self.base_weight:
            descriptors = list(self.descriptor_to_controller.keys())
            weights = np.array(
                [
                    1.0 if descriptions[desc] > 0 else self.base_weight
                    for desc in descriptors
                ]
            )
            weights /= weights.sum()
            actions = np.array(
                [
                    run_controller(self.descriptor_to_controller[desc], obs)
                    for desc in descriptors
                ]
            )
            weighted_action = np.einsum("i,ik->k", weights, actions)
            return weighted_action, info
        else:
            return run_controller(controller_name, obs), info


def evaluate_policy(env_name, episodes):
    print('Evaluating', env_name)
    successes = []
    controller_counts = defaultdict(int)
    candidate_counts = defaultdict(int)
    for episode in episodes:
        success = False
        for data in episode:
            success |= data.get("success", 0) > 0
            if "controller_name" in data:
                controller_counts[data["controller_name"]] += 1
            for candidate in data.get("candidate_controllers", []):
                candidate_counts[candidate] += 1
        successes.append(success)
    print("Success rate for", env_name, ":", np.mean(successes))
    print("controller_counts:")
    pprint(dict(controller_counts))
    print("candidate_counts:")
    pprint(dict(candidate_counts))
    return np.mean(successes)


def find_most_likely_plans(*, envs=",".join(MT10_ENV_NAMES), seed=100):
    env_names = list(envs.split(","))
    # For each descriptor, record how many observations with that descriptor each
    # controller is active
    # For each controller, look through each of these descriptor distributions,
    # and choose the best descriptor
    # Compose into policy, and count timesteps where policy disagrees with
    # original tree
    # for env_name in ['button-press-topdown']:
    success_rates = {}
    controller_maps = {}
    for env_name in env_names:
        desc_to_con_count = defaultdict(lambda: defaultdict(int))
        tree = metaworld_controllers.DECISION_TREES[env_name]["function"]
        policy = SawyerUniversalV2Policy(env_name=env_name)
        env = make_env(env_name, seed)
        controller_total_counts = defaultdict(int)
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
                controller_name = tree(obs)
                descriptions = describe_obs(env_name, obs)
                for (desc, value) in descriptions.items():
                    desc_to_con_count[desc][controller_name] += value
                controller_total_counts[controller_name] += 1
        policy_desc_to_con = {}
        for con_name in controller_names_for_env(env_name):
            # Maximize number of timesteps where the description is present for this
            # controller and no other controllers.
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
                    "for controller",
                    repr(con_name),
                    "(matches for",
                    counts[con_name],
                    "/",
                    controller_total_counts[con_name],
                    "timesteps)",
                )
                policy_desc_to_con[descriptor] = con_name
                num_chosen += 1
                if num_chosen >= 1:
                    break
        print(policy_desc_to_con)
        controller_maps[env_name] = policy_desc_to_con
        desc_policy = DescriptorPolicy(policy_desc_to_con, env_name=env_name)
        controller_prob = 0.1
        print("Weighting incorrect controller by", controller_prob)
        desc_policy.base_weight = controller_prob
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
        # for controller_prob in np.linspace(0, 1, 11):
        # print('Weighting incorrect controller by', controller_prob)
        # desc_policy.base_weight = controller_prob
        # success = evaluate_policy(env_name, 10,
        # lambda: sample_noisy_policy(env, desc_policy, 0.10))
        # desc_policy.base_weight = None
        # print('Using correct controller with prob', controller_prob)
        # desc_policy.controller_choice_prob = controller_prob
        # success = evaluate_policy(env_name, 10,
        # lambda: sample_noisy_policy(env, desc_policy, 0.10))
        # if controller_prob == 1.0:
        # success_rates[env_name] = success
    print(success_rates)
    print(controller_maps)
    with open(os.path.expanduser("~/data/controller_map.pkl"), "wb") as f:
        pickle.dump(controller_maps, f)


def test_smoke():
    seed = 100
    with tqdm(total=len(MT50_ENV_NAMES) * 500) as pbar:
        for env_name in MT50_ENV_NAMES:
            env = make_env(env_name, seed)
            # conditions = tuple(enumerate_descriptors(env_name)[:4])
            policy = metaworld_universal_policy.SawyerUniversalV2Policy(
                env_name=env_name
            )
            observation = env.reset()
            for i in range(env.max_episode_length):
                action, _ = policy.get_action(observation)
                observation, r, done, info = env.step(action)
                # eval_conditions(env_name, conditions, observation)
                describe_obs(env_name, observation)
                pbar.update(1)
                # print('-' * 80)
                # for (desc, truth_value) in describe_obs(env_name, observation).items():
                # print(f"{desc}:", bool(truth_value))
                # print('-' * 80)


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
    seed=jax_utils.DEFAULT_SEED,
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


if __name__ == "__main__":
    clize.run(find_most_likely_plans)
    # clize.run(test_parallel)
    # clize.run(test_smoke)
