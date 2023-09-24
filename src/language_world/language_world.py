from dataclasses import dataclass
from typing import Dict, Union, Callable, Tuple, List
import difflib

import numpy as np

# Hard-coded here to avoid a dependency on Meta-World
MT50_ENV_NAMES = [
    "assembly",
    "basketball",
    "bin-picking",
    "box-close",
    "button-press-topdown",
    "button-press-topdown-wall",
    "button-press",
    "button-press-wall",
    "coffee-button",
    "coffee-pull",
    "coffee-push",
    "dial-turn",
    "disassemble",
    "door-close",
    "door-lock",
    "door-open",
    "door-unlock",
    "hand-insert",
    "drawer-close",
    "drawer-open",
    "faucet-open",
    "faucet-close",
    "hammer",
    "handle-press-side",
    "handle-press",
    "handle-pull-side",
    "handle-pull",
    "lever-pull",
    "peg-insert-side",
    "pick-place-wall",
    "pick-out-of-hole",
    "reach",
    "push-back",
    "push",
    "pick-place",
    "plate-slide",
    "plate-slide-side",
    "plate-slide-back",
    "plate-slide-back-side",
    "peg-unplug-side",
    "soccer",
    "stick-push",
    "stick-pull",
    "push-wall",
    "reach-wall",
    "shelf-place",
    "sweep-into",
    "sweep",
    "window-open",
    "window-close",
]

MT10_ENV_NAMES = [
    "reach",
    "push",
    "pick-place",
    "door-open",
    "drawer-open",
    "drawer-close",
    "button-press-topdown",
    "peg-insert-side",
    "window-open",
    "window-close",
]


EDIT_DISTANCE_PROJ_CACHE = {}

def edit_distance_project(src, targets):
    cache_key = (src, tuple(targets))
    if cache_key in EDIT_DISTANCE_PROJ_CACHE:
        return EDIT_DISTANCE_PROJ_CACHE[cache_key]
    matches = sorted(
        targets,
        key=lambda tgt: difflib.SequenceMatcher(None, tgt, src).ratio(),
        reverse=True,
    )
    EDIT_DISTANCE_PROJ_CACHE[cache_key] = matches
    return matches

### Task Descriptions

TASK_DESCRIPTIONS = {
    "door-open": "open the door",
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
    "window-open": "slide the window open",
    "window-close": "slide the window closed",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}


### Scripted Skills Start Here

@dataclass
class ControlParams:

    target_xyz: np.ndarray
    grab_effort: float
    control_coeff: float

    def __post_init__(self):
        self.target_xyz = np.asarray(self.target_xyz, dtype="float32")
        self.grab_effort = float(self.grab_effort)
        self.control_coeff = float(self.control_coeff)

    def run(self, from_xyz):
        """Computes action components that help move from 1 position to another

        Args:
            from_xyz (np.ndarray): The coordinates to move from (usually current position)

        Returns:
            (np.ndarray): Response that will decrease abs(self.target_xyz - from_xyz)

        """
        error = self.target_xyz - from_xyz
        response = self.control_coeff * error

        return response


@dataclass
class ParsedObs:

    hand_pos: np.ndarray
    gripper_distance_apart: np.ndarray
    obj1_pos: np.ndarray
    obj1_rot: np.ndarray
    obj2_pos: np.ndarray
    obj2_rot: np.ndarray
    last_hand_pos: np.ndarray
    last_gripper: np.ndarray
    last_obj1_pos: np.ndarray
    last_obj1_rot: np.ndarray
    last_obj2_pos: np.ndarray
    last_obj2_rot: np.ndarray
    goal_pos: np.ndarray

    @classmethod
    def from_obs(cls, obs: np.ndarray):
        return cls(**{
            "hand_pos": obs[:3],
            "gripper_distance_apart": obs[3],
            "obj1_pos": obs[4:7],
            "obj1_rot": obs[7:11],
            "obj2_pos": obs[11:14],
            "obj2_rot": obs[14:18],
            "last_hand_pos": obs[18:21],
            "last_gripper": obs[21],
            "last_obj1_pos": obs[22:25],
            "last_obj1_rot": obs[25:29],
            "last_obj2_pos": obs[29:32],
            "last_obj2_rot": obs[32:36],
            "goal_pos": obs[36:39],
        })



# Scripted skill functions that map from parsed observations to control parameters
SCRIPTED_SKILLS: Dict[str, Callable[[ParsedObs], ControlParams]] = {}
# Mapping from scripted skill names to primary task for that skill
SCRIPTED_SKILL_TASKS: Dict[str, str] = {}
# Functions for each task in MT10 that choose a scripted skill given a parsed observation
SKILL_SELECTORS: Dict[str, Callable[[ParsedObs], str]] = {}


def _declare_skill(task_name, name):
    def decorator(func):
        assert name not in SCRIPTED_SKILLS
        assert task_name in MT50_ENV_NAMES
        SCRIPTED_SKILLS[name] = func
        SCRIPTED_SKILL_TASKS[name] = task_name
        return func

    return decorator


def _declare_skill_selector(task_name):
    def decorator(func):
        assert task_name not in SKILL_SELECTORS
        SKILL_SELECTORS[task_name] = func
        return func

    return decorator


@_declare_skill("drawer-close", "put the gripper in front of the drawer")
def front_drawer(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])
    return ControlParams(np.asarray([pos_curr[0], pos_curr[1], pos_drwr[2] + 0.5]), 1, control_coeff=25)


@_declare_skill("drawer-close", "put the gripper above the drawer handle")
def above_drawer_handle(obs_parsed):
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, -0.075, 0.23])
    return ControlParams(pos_drwr + np.array([0.0, -0.075, 0.23]), 1, control_coeff=25)


@_declare_skill("drawer-close", "grab drawer handle")
def cage_gripper_handle(obs_parsed):
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])
    return ControlParams(pos_drwr + np.array([0.0, -0.075, 0.0]), 1, control_coeff=25)


@_declare_skill("drawer-close", "push drawer closed")
def push_drawer(obs_parsed):
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])
    return ControlParams(pos_drwr, 1, control_coeff=25)


@_declare_skill_selector("drawer-close")
def drawer_close(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])

    # if further forward than the drawer...
    if pos_curr[1] > pos_drwr[1]:
        if pos_curr[2] < pos_drwr[2] + 0.23:
            # rise up quickly (Z direction)
            return "put the gripper in front of the drawer"
        else:
            # move to front edge of drawer handle, but stay high in Z
            return "put the gripper above the drawer handle"
    # drop down to touch drawer handle
    elif abs(pos_curr[2] - pos_drwr[2]) > 0.04:
        return "grab drawer handle"
    # push toward drawer handle's centroid
    else:
        return "push drawer closed"


@_declare_skill("peg-insert-side", "put gripper above peg")
def cage_peg(obs_parsed):
    pos_peg = obs_parsed.obj1_pos
    return ControlParams(pos_peg + np.array([0.0, 0.0, 0.3]), -1, control_coeff=25)


@_declare_skill("peg-insert-side", "grab peg")
def grab_peg(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_peg = obs_parsed.obj1_pos
    grab_effort = np.interp(
        abs(pos_curr[2] - pos_peg[2]), xp=np.array([0.14, 0.15]), fp=np.array([0.6, -1])
    )
    return ControlParams(pos_peg, grab_effort, control_coeff=25)


@_declare_skill("peg-insert-side", "align peg to hole")
def align_peg(obs_parsed):
    pos_hole = np.array([-0.35, obs_parsed.goal_pos[1], 0.16])
    return ControlParams(pos_hole + np.array([0.4, 0.0, 0.0]), 0.6, control_coeff=25)


@_declare_skill("peg-insert-side", "insert peg into hole")
def insert_peg(obs_parsed):
    pos_hole = np.array([-0.35, obs_parsed.goal_pos[1], 0.16])
    return ControlParams(pos_hole, 0.6, control_coeff=25)


@_declare_skill_selector("peg-insert-side")
def peg_insert_side(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_peg = obs_parsed.obj1_pos
    # lowest X is -.35, doesn't matter if we overshoot
    # Y is given by hole_vec
    # Z is constant at .16
    pos_hole = np.array([-0.35, obs_parsed.goal_pos[1], 0.16])

    if np.linalg.norm(pos_curr[:2] - pos_peg[:2]) > 0.04:
        return "put gripper above peg"
    elif abs(pos_curr[2] - pos_peg[2]) > 0.025:
        return "grab peg"
    elif np.linalg.norm(pos_peg[1:] - pos_hole[1:]) > 0.03:
        return "align peg to hole"
    else:
        return "insert peg into hole"


@_declare_skill_selector("reach")
def reach(obs_parsed):
    return "reach to goal"


@_declare_skill("reach", "reach to goal")
def reach_skill(obs_parsed):
    return ControlParams(obs_parsed.goal_pos, 0, control_coeff=5)


@_declare_skill("window-open", "move gripper to right of window handle")
def right_of_window_handle(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([-0.03, -0.03, -0.08])
    return ControlParams(pos_wndw + np.array([0.0, 0.0, 0.3]), 1.0, control_coeff=25)


@_declare_skill("window-open", "slide window left")
def slide_window_left(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([-0.03, -0.03, -0.08])
    return ControlParams(pos_wndw, 1.0, control_coeff=25)


@_declare_skill("window-open", "push window left harder")
def push_window_left(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([-0.03, -0.03, -0.08])
    return ControlParams(pos_wndw + np.array([0.1, 0.0, 0.0]), 1.0, control_coeff=25)


@_declare_skill_selector("window-open")
def window_open(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_wndw = obs_parsed.obj1_pos + np.array([-0.03, -0.03, -0.08])

    if np.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to right of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window left"
    else:
        return "push window left harder"


@_declare_skill("window-close", "move gripper to left of window handle")
def left_of_window_handle(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([+0.03, -0.03, -0.08])
    return ControlParams(pos_wndw + np.array([0.0, 0.0, 0.25]), 1.0, control_coeff=25)


@_declare_skill("window-close", "slide window right")
def slide_window_right(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([+0.03, -0.03, -0.08])
    return ControlParams(pos_wndw, 1.0, control_coeff=25)


@_declare_skill("window-close", "push window right harder")
def slide_window_right_harder(obs_parsed):
    pos_wndw = obs_parsed.obj1_pos + np.array([+0.03, -0.03, -0.08])
    return ControlParams(pos_wndw + np.array([-0.1, 0.0, 0.0]), 1.0, control_coeff=25)


@_declare_skill_selector("window-close")
def window_close(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_wndw = obs_parsed.obj1_pos + np.array([+0.03, -0.03, -0.08])

    if np.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to left of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window right"
    else:
        return "push window right harder"


@_declare_skill_selector("drawer-open")
def drawer_open(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])

    # align end effector's Z axis with drawer handle's Z axis
    if np.linalg.norm(pos_curr[:2] - pos_drwr[:2]) > 0.06:
        return "put gripper above drawer handle"
    # drop down to touch drawer handle
    elif abs(pos_curr[2] - pos_drwr[2]) > 0.04:
        return "put gripper around drawer handle"
    # push toward a point just behind the drawer handle
    # also increase control_coeff value to apply more force
    else:
        return "pull away from drawer"


@_declare_skill("drawer-open", "put gripper above drawer handle")
def gripper_above_drawer_handle(obs_parsed):
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])
    to_pos = pos_drwr + np.array([0.0, 0.0, 0.3])
    return ControlParams(to_pos, -1, control_coeff=4)


@_declare_skill("drawer-open", "put gripper around drawer handle")
def gripper_around_drawer_handle(obs_parsed):
    return ControlParams(obs_parsed.obj1_pos, -1, control_coeff=4)


@_declare_skill("drawer-open", "pull away from drawer")
def pull_away_from_drawer(obs_parsed):
    pos_drwr = obs_parsed.obj1_pos + np.array([0.0, 0.0, -0.02])
    to_pos = pos_drwr + np.array([0.0, -0.06, 0.0])
    return ControlParams(to_pos, -1, control_coeff=50)


@_declare_skill_selector("door-open")
def door_open(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_door = obs_parsed.obj1_pos - np.array([0.05, 0, 0])

    # align end effector's Z axis with door handle's Z axis
    if np.linalg.norm(pos_curr[:2] - pos_door[:2]) > 0.12:
        return "put gripper above door handle"
    # drop down on front edge of door handle
    elif abs(pos_curr[2] - pos_door[2]) > 0.04:
        return "put gripper around door handle"
    # push from front edge toward door handle's centroid
    else:
        return "pull door open"


@_declare_skill("door-open", "put gripper above door handle")
def gripper_above_door_handle(obs_parsed):
    pos_door = obs_parsed.obj1_pos - np.array([0.05, 0, 0])
    return ControlParams(pos_door + np.array([0.06, 0.02, 0.2]), 1, control_coeff=4)


@_declare_skill("door-open", "put gripper around door handle")
def gripper_around_door_handle(obs_parsed):
    pos_door = obs_parsed.obj1_pos - np.array([0.05, 0, 0])
    return ControlParams(pos_door + np.array([0.06, 0.02, 0]), 1, control_coeff=4)


@_declare_skill("door-open", "pull door open")
def pull_door_open(obs_parsed):
    pos_door = obs_parsed.obj1_pos - np.array([0.05, 0, 0])
    return ControlParams(pos_door, 1, control_coeff=4)


@_declare_skill_selector("push")
def push(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_puck = obs_parsed.obj1_pos + np.array([-0.005, 0, 0])
    pos_goal = obs_parsed.goal_pos

    # If error in the XY plane is greater than 0.02, place end effector above the puck
    if np.linalg.norm(pos_curr[:2] - pos_puck[:2]) > 0.02:
        return "put the gripper above the puck"
    # Once XY error is low enough, drop end effector down on top of puck
    elif abs(pos_curr[2] - pos_puck[2]) > 0.04:
        return "push the gripper into the puck"
    # Move to the goal
    else:
        return "slide the puck to the goal"


@_declare_skill("push", "put the gripper above the puck")
def gripper_above_puck(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_puck = obs_parsed.obj1_pos + np.array([-0.005, 0, 0])
    grab_effort = 0
    grab_effort = 0
    return ControlParams(pos_puck + np.array([0.0, 0.0, 0.2]), grab_effort, control_coeff=10)


@_declare_skill("push", "push the gripper into the puck")
def push_down_on_puck(obs_parsed):
    pos_puck = obs_parsed.obj1_pos + np.array([-0.005, 0, 0])
    grab_effort = 0.6
    grab_effort = 0
    return ControlParams(pos_puck + np.array([0.0, 0.0, 0.03]), grab_effort, control_coeff=10)


@_declare_skill("push", "slide the puck to the goal")
def slide_puck_to_goal(obs_parsed):
    pos_goal = obs_parsed.goal_pos
    grab_effort = 0.6
    return ControlParams(pos_goal, grab_effort, control_coeff=10)


@_declare_skill_selector("button-press-topdown")
def button_press_topdown(obs_parsed):
    pos_curr = obs_parsed.hand_pos
    pos_button = obs_parsed.obj1_pos

    if np.linalg.norm(pos_curr[:2] - pos_button[:2]) > 0.04:
        return "put gripper above button"
    else:
        return "push down on button"


@_declare_skill("button-press-topdown", "put gripper above button")
def gripper_above_button(obs_parsed):
    return ControlParams(obs_parsed.obj1_pos + np.array([0.0, 0.0, 0.1]), 1.0, control_coeff=25)


@_declare_skill("button-press-topdown", "push down on button")
def push_down_on_button(obs_parsed):
    return ControlParams(obs_parsed.obj1_pos, 1.0, control_coeff=25)


@_declare_skill_selector("pick-place")
def pick_place(obs):
    pos_curr = obs.hand_pos
    pos_puck = obs.obj1_pos + np.array([-0.005, 0, 0])
    gripper_separation = obs.gripper_distance_apart
    # If error in the XY plane is greater than 0.02, place end effector above the puck
    if np.linalg.norm(pos_curr[:2] - pos_puck[:2]) > 0.02:
        return "place gripper above puck"
    # Once XY error is low enough, drop end effector down on top of puck
    elif abs(pos_curr[2] - pos_puck[2]) > 0.05 and pos_puck[-1] < 0.04:
        return "drop gripper around puck"
    # Wait for gripper to close before continuing to move
    elif gripper_separation > 0.73:
        return "close gripper around puck"
    # Move to goal
    else:
        return "place puck at goal"


@_declare_skill("pick-place", "place gripper above puck")
def place_gripper_above_puck(obs):
    pos_puck = obs.obj1_pos + np.array([-0.005, 0, 0])
    return ControlParams(pos_puck + np.array([0.0, 0.0, 0.1]), 0.0, control_coeff=10)


@_declare_skill("pick-place", "drop gripper around puck")
def drop_gripper_argound_puck(obs):
    pos_puck = obs.obj1_pos + np.array([-0.005, 0, 0])
    return ControlParams(pos_puck + np.array([0.0, 0.0, 0.03]), 0.0, control_coeff=10)


@_declare_skill("pick-place", "close gripper around puck")
def close_gripper_around_puck(obs):
    return ControlParams(obs.hand_pos, 1.0, control_coeff=10)


@_declare_skill("pick-place", "place puck at goal")
def place_puck_at_goal(obs):
    return ControlParams(obs.goal_pos, 1.0, control_coeff=10)


# This is the intended public API for scripted skills (but use the code in this
# module as you see fit).

SCRIPTED_SKILL_NAMES = list(SCRIPTED_SKILLS.keys())

def nearest_skill(skill_description: str):
    return edit_distance_project(skill_description, SCRIPTED_SKILL_NAMES)

def run_scripted_skill(
    skill_name: str, obs: np.ndarray
) -> np.ndarray:
    if isinstance(obs, ParsedObs):
        parsed_obs = obs
    else:
        parsed_obs = ParsedObs.from_obs(obs)
    skill_func = SCRIPTED_SKILLS[skill_name]
    control_params = skill_func(parsed_obs)
    delta_xyz = control_params.run(parsed_obs.hand_pos)

    return np.concatenate([delta_xyz, np.array([control_params.grab_effort])])


### Query Answering Function

_COORDINATE_RELATIONS = [
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


_OBJECT_NAMES = {
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

_OBJECT_NAMES_TO_PARSE_NAME = {
    task_name: {v: k for (k, v) in env_map.items()}
    for (task_name, env_map) in _OBJECT_NAMES.items()
}

assert len(_OBJECT_NAMES) == 50
assert set(_OBJECT_NAMES.keys()) == set(MT50_ENV_NAMES)

_WALL_ENVS = {
    "reach-wall",
    "pick-place-wall",
    "push-wall",
    "button-press-wall",
    "button-press-topdown-wall",
}

MT50_TASK_DESCRIPTIONS = {
    "door-open": "open the door",
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
    "window-open": "slide the window open",
    "window-close": "slide the window closed",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}

assert set(TASK_DESCRIPTIONS.keys()) == set(MT50_ENV_NAMES)
assert len(TASK_DESCRIPTIONS) == 50


def describe_obs(task_name, obs):
    queries = enumerate_all_queries(task_name)
    return dict(zip(queries, eval_queries(task_name, queries, obs)))


_POSITIVE_RELATION_SUBSTR = [f" is {rel} " for rel in _COORDINATE_RELATIONS]
_NEGATIVE_RELATION_SUBSTR = [f" is not {rel} " for rel in _COORDINATE_RELATIONS]

def _get_object_location(task_name: str, object_name: str, parsed_obs, fuzzy: bool = False):
    try:
        parse_name = _OBJECT_NAMES_TO_PARSE_NAME[task_name][object_name]
    except KeyError as exc:
        if object_name == "the robot's gripper":
            parse_name = "hand_pos"
        elif object_name.startswith("the "):
            return _get_object_location(
                task_name, object_name.split("the ")[1], parsed_obs, fuzzy=fuzzy
            )
        elif task_name == "peg-insert-side" and object_name == "hole":
            return np.array([-0.35, parsed_obs.goal_pos[1], 0.16])
        elif task_name in _WALL_ENVS and object_name == "wall":
            if (
                task_name == "reach-wall"
                or task_name == "push-wall"
                or task_name == "pick-place-wall"
            ):
                return np.array([0.1, 0.75, 0.06])
            elif task_name == "button-press-wall":
                return np.array([0.1, 0.6, 0.0])
            elif task_name == "button-press-topdown-wall":
                return np.array([0.1, 0.7, 0.0])
            else:
                raise NotImplementedError(f"Unknown wall environment: {task_name}")
        elif fuzzy:
            object_names = list(_OBJECT_NAMES_TO_PARSE_NAME[task_name].keys())
            matches = edit_distance_project(object_name, object_names)
            parse_name = _OBJECT_NAMES_TO_PARSE_NAME[task_name][matches[0]]
        else:
            raise exc
    # print(f'{object_name!r} (a.k.a. {parse_name!r}) is located at {obs[parse_name]}')
    return getattr(parsed_obs, parse_name)


def _eval_relation(rel: str, xyz1: np.ndarray, xyz2: np.ndarray):
    assert rel.strip() == rel
    if rel == "near":
        return np.linalg.norm(xyz1 - xyz2) < 0.04
    elif rel == "around":
        return np.linalg.norm(xyz1 - xyz2 + np.array([0, 0, 0.02])) < 0.03
    elif rel == "left of":
        return xyz1[0] - xyz2[0] > 0.04
    elif rel == "right of":
        return xyz1[0] - xyz2[0] < -0.04
    elif rel == "behind":
        return (xyz1[1] - xyz2[1] > 0.04) * (
            np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "in front of":
        return (xyz1[1] - xyz2[1] < -0.04) * (
            np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "above":
        return (np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] > 0.0)
    elif rel == "below":
        return (np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] < 0)
    elif rel == "vertically aligned with":
        return np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.06
    elif rel == "almost vertically aligned with":
        return np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.12
    elif rel == "mostly below":
        return xyz1[2] < xyz2[2] + 0.23
    elif rel == "horizontally aligned with":
        return np.linalg.norm(xyz1[1:] - xyz2[1:]) < 0.03
    elif rel == "forward aligned with":
        return np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.03
    else:
        raise TypeError(f"Unknown coordinate relation {rel}")


def eval_queries(task_name: str, queries: Union[List[str], Tuple[str, ...]],
                    obs: Union[np.ndarray, ParsedObs], fuzzy=False):
    if isinstance(obs, ParsedObs):
        parsed_obs = obs
    else:
        parsed_obs = ParsedObs.from_obs(obs)
    results = []
    for full_query in queries:
        base_queries = full_query.split(" and ")

        base_results = []
        for query in base_queries:
            if query == "the robot's gripper is open":
                base_results.append(parsed_obs.gripper_distance_apart > 0.75)
            elif query == "the robot's gripper is closed":
                base_results.append(parsed_obs.gripper_distance_apart <= 0.75)
            elif query.endswith(" is not touching the table"):
                object_name = query.split(" is not touching the table")[0]
                xyz = _get_object_location(task_name, object_name, parsed_obs, fuzzy)
                base_results.append(xyz[2] > 0.02)
            elif query.endswith(" is touching the table"):
                object_name = query.split(" is touching the table")[0]
                xyz = _get_object_location(task_name, object_name, parsed_obs, fuzzy)
                base_results.append(xyz[2] <= 0.02)
            elif any(substr in query for substr in _NEGATIVE_RELATION_SUBSTR):
                neg_relations = [
                    rel for rel in _COORDINATE_RELATIONS if f" is not {rel} " in query
                ]
                assert len(neg_relations) >= 1
                rel = neg_relations[0]
                obj_name1, obj_name2 = query.split(f" is not {rel} ")
                xyz1 = _get_object_location(task_name, obj_name1, parsed_obs, fuzzy)
                xyz2 = _get_object_location(task_name, obj_name2, parsed_obs, fuzzy)
                base_results.append(1 - _eval_relation(rel, xyz1, xyz2))
            elif any(substr in query for substr in _POSITIVE_RELATION_SUBSTR):
                pos_relations = [
                    rel for rel in _COORDINATE_RELATIONS if f" is {rel} " in query
                ]
                assert len(pos_relations) >= 1
                rel = pos_relations[0]
                obj_name1, obj_name2 = query.split(f" is {rel} ")
                xyz1 = _get_object_location(task_name, obj_name1, parsed_obs, fuzzy)
                xyz2 = _get_object_location(task_name, obj_name2, parsed_obs, fuzzy)
                base_results.append(_eval_relation(rel, xyz1, xyz2))
            elif fuzzy:
                possible_queries = enumerate_all_queries(task_name)
                matches = edit_distance_project(query, possible_queries)
                base_results.append(
                    eval_queries(task_name, [matches[0]], parsed_obs, fuzzy=False)[0]
                )
            else:
                raise TypeError(f"Could not eval query {query}")
        results.append(np.all(np.array(base_results)))
    return np.array(results)


def enumerate_base_queries(task_name: str) -> List[str]:
    object_names = ["robot's gripper"] + list(_OBJECT_NAMES[task_name].values())
    object_names = ["the " + obj_name for obj_name in object_names]
    if task_name == "peg-insert-side":
        object_names.append("hole")
    elif (
        task_name == "reach-wall"
        or task_name == "push-wall"
        or task_name == "pick-place-wall"
        or task_name == "button-press-wall"
        or task_name == "button-press-topdown-wall"
    ):
        object_names.append("wall")
    descriptors = []
    for name1 in object_names:
        for name2 in object_names:
            if name1 == name2:
                continue
            for rel in _COORDINATE_RELATIONS:
                if rel == "around" and name1 != "the robot's gripper":
                    continue
                descriptors.append(f"{name1} is {rel} {name2}")
                descriptors.append(f"{name1} is not {rel} {name2}")
    for (key, name) in _OBJECT_NAMES[task_name].items():
        if key == "goal_pos":
            continue
        descriptors.append(f"{name} is touching the table")
        descriptors.append(f"{name} is not touching the table")

    descriptors.append("the robot's gripper is open")
    descriptors.append("the robot's gripper is closed")
    return descriptors


def enumerate_all_queries(task_name: str) -> List[str]:
    descriptors = enumerate_base_queries(task_name)
    conjunction_descriptors = []
    for desc1 in descriptors:
        for desc2 in descriptors:
            conjunction_descriptors.append(f"{desc1} and {desc2}")
    all_descriptors = descriptors + conjunction_descriptors
    return all_descriptors


try:
    import pytest

    @pytest.mark.parametrize("skill_name", SCRIPTED_SKILL_NAMES)
    def test_can_run_every_skill(skill_name: str):
        run_scripted_skill(skill_name, np.zeros(39))

    @pytest.mark.parametrize("task", MT50_ENV_NAMES)
    def test_can_eval_fuzzy_condition(task: str):
        eval_queries(task, ["", "nonsense query"], np.zeros(39), fuzzy=True)

    @pytest.mark.parametrize("task", MT50_ENV_NAMES)
    def test_can_eval_every_enumerated(task: str):
        queries = enumerate_all_queries(task)
        for query in queries:
            eval_queries(task, [query], np.zeros(39), fuzzy=False)
        eval_queries(task, ["the robot's gripper is not touching the table"], np.zeros(39), fuzzy=False)
except ImportError:
    pass
