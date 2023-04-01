from dataclasses import dataclass
from typing import Dict, Optional, Union
import numpy as np

from metaworld.envs.mujoco.env_dict import MT10_V2, ALL_V2_ENVIRONMENTS
from metaworld.policies.policy import Policy, assert_fully_parsed


def move(from_xyz, to_xyz, p):
    """Computes action components that help move from 1 position to another

    Args:
        from_xyz (np.ndarray): The coordinates to move from (usually current position)
        to_xyz (np.ndarray): The coordinates to move to
        p (float): constant to scale response

    Returns:
        (np.ndarray): Response that will decrease abs(to_xyz - from_xyz)

    """
    error = to_xyz - from_xyz
    response = p * error

    return response


def act(target_xyz, grab_effort, *, p):
    if isinstance(grab_effort, int):
        grab_effort = float(grab_effort)
    return {
        "target_xyz": np.asarray(target_xyz, dtype="float32"),
        "grab_effort": grab_effort,
        "control_coeff": float(p),
    }


SCRIPTED_SKILLS = {}
DECISION_TREES = {}


def declare_skill(env_name, name):
    def decorator(func):
        assert name not in SCRIPTED_SKILLS
        SCRIPTED_SKILLS[name] = {
            "function": func,
            "env-name": env_name,
        }
        return func

    return decorator


def declare_policy(env_name):
    def decorator(func):
        assert env_name not in DECISION_TREES
        DECISION_TREES[env_name] = {
            "function": func,
        }
        return func

    return decorator


@declare_skill("drawer-close", "put the gripper in front of the drawer")
def front_drawer(o_d):
    pos_curr = o_d["hand_pos"]
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])
    return act([pos_curr[0], pos_curr[1], pos_drwr[2] + 0.5], 1, p=25)


@declare_skill("drawer-close", "put the gripper above the drawer handle")
def above_drawer_handle(o_d):
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, -0.075, 0.23])
    return act(pos_drwr + np.array([0.0, -0.075, 0.23]), 1, p=25)


@declare_skill("drawer-close", "grab drawer handle")
def cage_gripper_handle(o_d):
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])
    return act(pos_drwr + np.array([0.0, -0.075, 0.0]), 1, p=25)


@declare_skill("drawer-close", "push drawer closed")
def push_drawer(o_d):
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])
    return act(pos_drwr, 1, p=25)


@declare_policy("drawer-close")
def drawer_close(o_d):
    pos_curr = o_d["hand_pos"]
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])

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


@declare_skill("peg-insert-side", "put gripper above peg")
def cage_peg(o_d):
    pos_peg = o_d["obj1_pos"]
    return act(pos_peg + np.array([0.0, 0.0, 0.3]), -1, p=25)


@declare_skill("peg-insert-side", "grab peg")
def grab_peg(o_d):
    pos_curr = o_d["hand_pos"]
    pos_peg = o_d["obj1_pos"]
    grab_effort = np.interp(
        abs(pos_curr[2] - pos_peg[2]), xp=np.array([0.14, 0.15]), fp=np.array([0.6, -1])
    )
    return act(pos_peg, grab_effort, p=25)


@declare_skill("peg-insert-side", "align peg to hole")
def cage_peg(o_d):
    pos_hole = np.array([-0.35, o_d["goal_pos"][1], 0.16])
    return act(pos_hole + np.array([0.4, 0.0, 0.0]), 0.6, p=25)


@declare_skill("peg-insert-side", "insert peg into hole")
def cage_peg(o_d):
    pos_hole = np.array([-0.35, o_d["goal_pos"][1], 0.16])
    return act(pos_hole, 0.6, p=25)


@declare_policy("peg-insert-side")
def peg_insert_side(o_d):
    pos_curr = o_d["hand_pos"]
    pos_peg = o_d["obj1_pos"]
    # lowest X is -.35, doesn't matter if we overshoot
    # Y is given by hole_vec
    # Z is constant at .16
    pos_hole = np.array([-0.35, o_d["goal_pos"][1], 0.16])

    if np.linalg.norm(pos_curr[:2] - pos_peg[:2]) > 0.04:
        return "put gripper above peg"
    elif abs(pos_curr[2] - pos_peg[2]) > 0.025:
        return "grab peg"
    elif np.linalg.norm(pos_peg[1:] - pos_hole[1:]) > 0.03:
        return "align peg to hole"
    else:
        return "insert peg into hole"


@declare_policy("reach")
def reach(o_d):
    return "reach to goal"


@declare_skill("reach", "reach to goal")
def reach_skill(o_d):
    return act(o_d["goal_pos"], 0, p=5)


@declare_skill("window-open", "move gripper to right of window handle")
def right_of_window_handle(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([-0.03, -0.03, -0.08])
    return act(pos_wndw + np.array([0.0, 0.0, 0.3]), 1.0, p=25)


@declare_skill("window-open", "slide window left")
def slide_window_left(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([-0.03, -0.03, -0.08])
    return act(pos_wndw, 1.0, p=25)


@declare_skill("window-open", "push window left harder")
def push_window_left(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([-0.03, -0.03, -0.08])
    return act(pos_wndw + np.array([0.1, 0.0, 0.0]), 1.0, p=25)


@declare_policy("window-open")
def window_open(o_d):
    pos_curr = o_d["hand_pos"]
    pos_wndw = o_d["obj1_pos"] + np.array([-0.03, -0.03, -0.08])

    if np.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to right of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window left"
    else:
        return "push window left harder"


@declare_skill("window-close", "move gripper to left of window handle")
def left_of_window_handle(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([+0.03, -0.03, -0.08])
    return act(pos_wndw + np.array([0.0, 0.0, 0.25]), 1.0, p=25)


@declare_skill("window-close", "slide window right")
def slide_window_right(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([+0.03, -0.03, -0.08])
    return act(pos_wndw, 1.0, p=25)


@declare_skill("window-close", "push window right harder")
def slide_window_right(o_d):
    pos_wndw = o_d["obj1_pos"] + np.array([+0.03, -0.03, -0.08])
    return act(pos_wndw + np.array([-0.1, 0.0, 0.0]), 1.0, p=25)


@declare_policy("window-close")
def window_close(o_d):
    pos_curr = o_d["hand_pos"]
    pos_wndw = o_d["obj1_pos"] + np.array([+0.03, -0.03, -0.08])

    if np.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to left of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window right"
    else:
        return "push window right harder"


@declare_policy("drawer-open")
def drawer_open(o_d):
    pos_curr = o_d["hand_pos"]
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])

    # align end effector's Z axis with drawer handle's Z axis
    if np.linalg.norm(pos_curr[:2] - pos_drwr[:2]) > 0.06:
        return "put gripper above drawer handle"
    # drop down to touch drawer handle
    elif abs(pos_curr[2] - pos_drwr[2]) > 0.04:
        return "put gripper around drawer handle"
    # push toward a point just behind the drawer handle
    # also increase p value to apply more force
    else:
        return "pull away from drawer"


@declare_skill("drawer-open", "put gripper above drawer handle")
def gripper_above_drawer_handle(o_d):
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])
    to_pos = pos_drwr + np.array([0.0, 0.0, 0.3])
    return act(to_pos, -1, p=4)


@declare_skill("drawer-open", "put gripper around drawer handle")
def gripper_around_drawer_handle(o_d):
    return act(o_d["obj1_pos"], -1, p=4)


@declare_skill("drawer-open", "pull away from drawer")
def gripper_above_drawer_handle(o_d):
    pos_drwr = o_d["obj1_pos"] + np.array([0.0, 0.0, -0.02])
    to_pos = pos_drwr + np.array([0.0, -0.06, 0.0])
    return act(to_pos, -1, p=50)


@declare_policy("door-open")
def door_open(o_d):
    pos_curr = o_d["hand_pos"]
    pos_door = o_d["obj1_pos"] - np.array([0.05, 0, 0])

    # align end effector's Z axis with door handle's Z axis
    if np.linalg.norm(pos_curr[:2] - pos_door[:2]) > 0.12:
        return "put gripper above door handle"
    # drop down on front edge of door handle
    elif abs(pos_curr[2] - pos_door[2]) > 0.04:
        return "put gripper around door handle"
    # push from front edge toward door handle's centroid
    else:
        return "pull door open"


@declare_skill("door-open", "put gripper above door handle")
def gripper_above_door_handle(o_d):
    pos_door = o_d["obj1_pos"] - np.array([0.05, 0, 0])
    return act(pos_door + np.array([0.06, 0.02, 0.2]), 1, p=4)


@declare_skill("door-open", "put gripper around door handle")
def gripper_around_door_handle(o_d):
    pos_door = o_d["obj1_pos"] - np.array([0.05, 0, 0])
    return act(pos_door + np.array([0.06, 0.02, 0]), 1, p=4)


@declare_skill("door-open", "pull door open")
def pull_door_open(o_d):
    pos_door = o_d["obj1_pos"] - np.array([0.05, 0, 0])
    return act(pos_door, 1, p=4)


@declare_policy("push")
def push(o_d):
    pos_curr = o_d["hand_pos"]
    pos_puck = o_d["obj1_pos"] + np.array([-0.005, 0, 0])
    pos_goal = o_d["goal_pos"]

    # If error in the XY plane is greater than 0.02, place end effector above the puck
    if np.linalg.norm(pos_curr[:2] - pos_puck[:2]) > 0.02:
        return "put the gripper above the puck"
    # Once XY error is low enough, drop end effector down on top of puck
    elif abs(pos_curr[2] - pos_puck[2]) > 0.04:
        return "push the gripper into the puck"
    # Move to the goal
    else:
        return "slide the puck to the goal"


@declare_skill("push", "put the gripper above the puck")
def gripper_above_puck(o_d):
    pos_curr = o_d["hand_pos"]
    pos_puck = o_d["obj1_pos"] + np.array([-0.005, 0, 0])
    grab_effort = 0
    grab_effort = 0
    return act(pos_puck + np.array([0.0, 0.0, 0.2]), grab_effort, p=10)


@declare_skill("push", "push the gripper into the puck")
def push_down_on_puck(o_d):
    pos_curr = o_d["hand_pos"]
    pos_puck = o_d["obj1_pos"] + np.array([-0.005, 0, 0])
    grab_effort = 0.6
    grab_effort = 0
    return act(pos_puck + np.array([0.0, 0.0, 0.03]), grab_effort, p=10)


@declare_skill("push", "slide the puck to the goal")
def slide_puck_to_goal(o_d):
    pos_goal = o_d["goal_pos"]
    pos_curr = o_d["hand_pos"]
    pos_puck = o_d["obj1_pos"] + np.array([-0.005, 0, 0])
    grab_effort = 0.6
    return act(pos_goal, grab_effort, p=10)


@declare_policy("button-press-topdown")
def button_press_topdown(o_d):
    pos_curr = o_d["hand_pos"]
    pos_button = o_d["obj1_pos"]

    if np.linalg.norm(pos_curr[:2] - pos_button[:2]) > 0.04:
        return "put gripper above button"
    else:
        return "push down on button"


@declare_skill("button-press-topdown", "put gripper above button")
def gripper_above_button(o_d):
    return act(o_d["obj1_pos"] + np.array([0.0, 0.0, 0.1]), 1.0, p=25)


@declare_skill("button-press-topdown", "push down on button")
def push_down_on_button(o_d):
    return act(o_d["obj1_pos"], 1.0, p=25)


@declare_policy("pick-place")
def pick_place(obs):
    pos_curr = obs["hand_pos"]
    pos_puck = obs["obj1_pos"] + np.array([-0.005, 0, 0])
    pos_goal = obs["goal_pos"]
    gripper_separation = obs["gripper_distance_apart"]
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


@declare_skill("pick-place", "place gripper above puck")
def place_gripper_above_puck(obs):
    pos_puck = obs["obj1_pos"] + np.array([-0.005, 0, 0])
    return act(pos_puck + np.array([0.0, 0.0, 0.1]), 0.0, p=10)


@declare_skill("pick-place", "drop gripper around puck")
def drop_gripper_argound_puck(obs):
    pos_puck = obs["obj1_pos"] + np.array([-0.005, 0, 0])
    return act(pos_puck + np.array([0.0, 0.0, 0.03]), 0.0, p=10)


@declare_skill("pick-place", "close gripper around puck")
def close_gripper_around_puck(obs):
    return act(obs["hand_pos"], 1.0, p=10)


@declare_skill("pick-place", "place puck at goal")
def place_puck_at_goal(obs):
    return act(obs["goal_pos"], 1.0, p=10)


def parse_obs(obs):
    return {
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
    }


def run_scripted_skill(
    skill_name: str, obs: Union[Dict[str, np.ndarray], np.ndarray]
) -> np.ndarray:
    if isinstance(obs, str):
        parsed_obs = parse_obs(obs)
    else:
        parsed_obs = obs
    skill_func = SCRIPTED_SKILLS[skill_name]["function"]
    skill_params = skill_func(parsed_obs)
    delta_xyz = move(
        parsed_obs["hand_pos"],
        skill_params["target_xyz"],
        skill_params["control_coeff"],
    )

    return np.concatenate([delta_xyz, np.array([skill_params["grab_effort"]])])


@dataclass
class SawyerUniversalV2Policy:

    env_name: Optional[str] = None

    def get_action(self, obs):
        o_d = parse_obs(obs)
        tree = DECISION_TREES[self.env_name]["function"]
        skill_name = tree(o_d)
        return run_scripted_skill(skill_name, o_d), {"skill_name": skill_name}


def trajectory_summary(env, policy, act_noise_pct, render=False, end_on_success=True):
    """Tests whether a given policy solves an environment
    Args:
        env (metaworld.envs.MujocoEnv): Environment to test
        policy (metaworld.policies.policies.Policy): Policy that's supposed to
            succeed in env
        act_noise_pct (np.ndarray): Decimal value(s) indicating std deviation of
            the noise as a % of action space
        render (bool): Whether to render the env in a GUI
        end_on_success (bool): Whether to stop stepping after first success
    Returns:
        (bool, np.ndarray, np.ndarray, int): Success flag, Rewards, Returns,
            Index of first success
    """
    success = False
    first_success = 0
    rewards = []

    for t, (r, done, info) in enumerate(
        trajectory_generator(env, policy, act_noise_pct, render)
    ):
        rewards.append(r)
        assert not env.isV2 or set(info.keys()) == {
            "success",
            "near_object",
            "grasp_success",
            "grasp_reward",
            "in_place_reward",
            "obj_to_target",
            "unscaled_reward",
        }
        success |= bool(info["success"])
        if not success:
            first_success = t
        if (success or done) and end_on_success:
            break

    rewards = np.array(rewards)
    returns = np.cumsum(rewards)

    return success, rewards, returns, first_success


def trajectory_generator(env, policy, act_noise_pct, render=False):
    """Tests whether a given policy solves an environment
    Args:
        env (metaworld.envs.MujocoEnv): Environment to test
        policy (metaworld.policies.policies.Policy): Policy that's supposed to
            succeed in env
        act_noise_pct (np.ndarray): Decimal value(s) indicating std deviation of
            the noise as a % of action space
        render (bool): Whether to render the env in a GUI
    Yields:
        (float, bool, dict): Reward, Done flag, Info dictionary
    """
    action_space_ptp = env.action_space.high - env.action_space.low

    env.reset()
    env.reset_model()
    o = env.reset()
    assert o.shape == env.observation_space.shape
    # assert env.observation_space.contains(o)

    for _ in range(env.max_path_length):
        a, _ = policy.get_action(o)
        a = np.random.normal(a, act_noise_pct * action_space_ptp)

        o, r, done, info = env.step(a)
        # assert env.observation_space.contains(o)
        if render:
            env.render()

        yield r, done, info


def make_env(env_name):
    e = ALL_V2_ENVIRONMENTS[env_name]()
    e._partially_observable = False
    e._freeze_rand_vec = False
    e._set_task_called = True
    return e


import pytest


@pytest.mark.parametrize(
    "env_name",
    MT10_V2.keys(),
)
@pytest.mark.parametrize("act_noise_pct", [0.0, 0.01, 0.05])
def test_universal_scripted_policy(env_name, act_noise_pct, iters=100):
    env = make_env(env_name)
    policy = SawyerUniversalV2Policy(env_name=env_name[:-3])

    successes = 0
    for _ in range(iters):
        successes += float(
            trajectory_summary(env, policy, act_noise_pct, render=False)[0]
        )
    print(successes)
    expected_success_rate = 0.8
    assert successes >= expected_success_rate * iters


if __name__ == "__main__":
    from pprint import pprint

    print("SCRITPED_SKILLS:")
    pprint(SCRIPTED_SKILLS)
