from dataclasses import dataclass
import jax.numpy as jnp

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
    return {
        'target_xyz': jnp.asarray(target_xyz, dtype='float32'),
        'grab_effort': float(grab_effort),
        'control_coeff': float(p)
    }

CONTROLLERS = {}
DECISION_TREES = {}

def declare_controller(env_name, name):
    def decorator(func):
        assert name not in CONTROLLERS
        CONTROLLERS[name] = {
            'function': func,
            'env-name': env_name,
        }
        return func
    return decorator

def declare_tree(env_name):
    def decorator(func):
        assert env_name not in DECISION_TREES
        DECISION_TREES[env_name] = {
            'function': func,
        }
        return func
    return decorator

@declare_controller("drawer-close", "put the gripper in front of the drawer")
def front_drawer(o_d):
    pos_curr = o_d['hand_pos']
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])
    return act([pos_curr[0], pos_curr[1], pos_drwr[2] + 0.5], 1, p=25)

@declare_controller("drawer-close", "put the gripper above the drawer handle")
def above_drawer_handle(o_d):
    pos_drwr = o_d['obj1_pos'] + jnp.array([0., -0.075, 0.23])
    return act(pos_drwr + jnp.array([0., -0.075, 0.23]), 1, p=25)

@declare_controller("drawer-close", "grab drawer handle")
def cage_gripper_handle(o_d):
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])
    return act(pos_drwr + jnp.array([0., -0.075, 0.]), 1, p=25)

@declare_controller("drawer-close", "push drawer closed")
def push_drawer(o_d):
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])
    return act(pos_drwr, 1, p=25)

@declare_tree("drawer-close")
def drawer_close(o_d):
    pos_curr = o_d['hand_pos']
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])

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

@declare_controller("peg-insert-side", "put gripper above peg")
def cage_peg(o_d):
    pos_peg = o_d['obj1_pos']
    return act(pos_peg + jnp.array([.0, .0, .3]), -1, p=25)

@declare_controller("peg-insert-side", "grab peg")
def grab_peg(o_d):
    pos_curr = o_d['hand_pos']
    pos_peg = o_d['obj1_pos']
    return act(pos_peg, .6, p=25)

@declare_controller("peg-insert-side", "align peg to hole")
def cage_peg(o_d):
    pos_hole = jnp.array([-.35, o_d['goal_pos'][1], .16])
    return act(pos_hole + jnp.array([.4, .0, .0]), .6, p=25)

@declare_controller("peg-insert-side", "insert peg into hole")
def cage_peg(o_d):
    pos_hole = jnp.array([-.35, o_d['goal_pos'][1], .16])
    return act(pos_hole, .6, p=25)

@declare_tree("peg-insert-side")
def peg_insert_side(o_d):
    pos_curr = o_d['hand_pos']
    pos_peg = o_d['obj1_pos']
    # lowest X is -.35, doesn't matter if we overshoot
    # Y is given by hole_vec
    # Z is constant at .16
    pos_hole = jnp.array([-.35, o_d['goal_pos'][1], .16])

    if jnp.linalg.norm(pos_curr[:2] - pos_peg[:2]) > .04:
        return "put gripper above peg"
    elif abs(pos_curr[2] - pos_peg[2]) > .025:
        return "grab peg"
    elif jnp.linalg.norm(pos_peg[1:] - pos_hole[1:]) > 0.03:
        return "align peg to hole"
    else:
        return "insert peg into hole"

@declare_tree('reach')
def reach(o_d):
    return "reach to goal"

@declare_controller('reach', 'reach to goal')
def reach_controller(o_d):
    return act(o_d['goal_pos'], 0, p=5)

@declare_controller('window-open', "move gripper to right of window handle")
def right_of_window_handle(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([-0.03, -0.03, -0.08])
    return act(pos_wndw + jnp.array([0., 0., 0.3]), 1., p=25)

@declare_controller('window-open', "slide window left")
def slide_window_left(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([-0.03, -0.03, -0.08])
    return act(pos_wndw, 1., p=25)

@declare_controller('window-open', "push window left harder")
def push_window_left(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([-0.03, -0.03, -0.08])
    return act(pos_wndw + jnp.array([0.1, 0., 0.]), 1., p=25)

@declare_tree('window-open')
def window_open(o_d):
    pos_curr = o_d['hand_pos']
    pos_wndw = o_d['obj1_pos'] + jnp.array([-0.03, -0.03, -0.08])

    if jnp.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to right of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window left"
    else:
        return "push window left harder"

@declare_controller('window-close', "move gripper to left of window handle")
def left_of_window_handle(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([+0.03, -0.03, -0.08])
    return act(pos_wndw + jnp.array([0., 0., 0.25]), 1., p=25)

@declare_controller('window-close', "slide window right")
def slide_window_right(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([+0.03, -0.03, -0.08])
    return act(pos_wndw, 1., p=25)

@declare_controller('window-close', "push window right harder")
def slide_window_right(o_d):
    pos_wndw = o_d['obj1_pos'] + jnp.array([+0.03, -0.03, -0.08])
    return act(pos_wndw + jnp.array([-0.1, 0., 0.]), 1., p=25)

@declare_tree('window-close')
def window_close(o_d):
    pos_curr = o_d['hand_pos']
    pos_wndw = o_d['obj1_pos'] + jnp.array([+0.03, -0.03, -0.08])

    if jnp.linalg.norm(pos_curr[:2] - pos_wndw[:2]) > 0.04:
        return "move gripper to left of window handle"
    elif abs(pos_curr[2] - pos_wndw[2]) > 0.02:
        return "slide window right"
    else:
        return "push window right harder"

@declare_tree('drawer-open')
def drawer_open(o_d):
    pos_curr = o_d['hand_pos']
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])

    # align end effector's Z axis with drawer handle's Z axis
    if jnp.linalg.norm(pos_curr[:2] - pos_drwr[:2]) > 0.06:
        return "put gripper above drawer handle"
    # drop down to touch drawer handle
    elif abs(pos_curr[2] - pos_drwr[2]) > 0.04:
        return "put gripper around drawer handle"
    # push toward a point just behind the drawer handle
    # also increase p value to apply more force
    else:
        return "pull away from drawer"

@declare_controller('drawer-open', "put gripper above drawer handle")
def gripper_above_drawer_handle(o_d):
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])
    to_pos = pos_drwr + jnp.array([0., 0., 0.3])
    return act(to_pos, -1, p=4)

@declare_controller('drawer-open', "put gripper around drawer handle")
def gripper_around_drawer_handle(o_d):
    return act(o_d['obj1_pos'], -1, p=4)

@declare_controller('drawer-open', "pull away from drawer")
def gripper_above_drawer_handle(o_d):
    pos_drwr = o_d['obj1_pos'] + jnp.array([.0, .0, -.02])
    to_pos = pos_drwr + jnp.array([0., -0.06, 0.])
    return act(to_pos, -1, p=50)

@declare_tree('door-open')
def door_open(o_d):
    pos_curr = o_d['hand_pos']
    pos_door = o_d['obj1_pos'] - jnp.array([0.05, 0, 0])

    # align end effector's Z axis with door handle's Z axis
    if jnp.linalg.norm(pos_curr[:2] - pos_door[:2]) > 0.12:
        return "put gripper above door handle"
    # drop down on front edge of door handle
    elif abs(pos_curr[2] - pos_door[2]) > 0.04:
        return "put gripper around door handle"
    # push from front edge toward door handle's centroid
    else:
        return "push door closed"

@declare_controller('door-open', "put gripper above door handle")
def gripper_above_door_handle(o_d):
    pos_door = o_d['obj1_pos'] - jnp.array([0.05, 0, 0])
    return act(pos_door + jnp.array([0.06, 0.02, 0.2]), 1, p=4)

@declare_controller('door-open', "put gripper around door handle")
def gripper_around_door_handle(o_d):
    pos_door = o_d['obj1_pos'] - jnp.array([0.05, 0, 0])
    return act(pos_door + jnp.array([0.06, 0.02, 0]), 1, p=4)

@declare_controller('door-open', "push door closed")
def push_door_closed(o_d):
    pos_door = o_d['obj1_pos'] - jnp.array([0.05, 0, 0])
    return act(pos_door, 1, p=4)

@declare_tree('push')
def push(o_d):
    pos_curr = o_d['hand_pos']
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    pos_goal = o_d['goal_pos']

    # If error in the XY plane is greater than 0.02, place end effector above the puck
    if jnp.linalg.norm(pos_curr[:2] - pos_puck[:2]) > 0.02:
        return "put the gripper above the puck"
    # Once XY error is low enough, drop end effector down on top of puck
    elif abs(pos_curr[2] - pos_puck[2]) > 0.04:
        return "push the gripper into the puck"
    # Move to the goal
    else:
        return "slide the puck to the goal"

@declare_controller('push', "put the gripper above the puck")
def gripper_above_puck(o_d):
    pos_curr = o_d['hand_pos']
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    grab_effort = 0
    return act(pos_puck + jnp.array([0., 0., 0.2]), grab_effort, p=10)

@declare_controller('push', "push the gripper into the puck")
def push_down_on_puck(o_d):
    pos_curr = o_d['hand_pos']
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    grab_effort = 0.6
    return act(pos_puck + jnp.array([0., 0., 0.03]), grab_effort, p=10)

@declare_controller('push', "slide the puck to the goal")
def slide_puck_to_goal(o_d):
    pos_goal = o_d['goal_pos']
    pos_curr = o_d['hand_pos']
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    grab_effort = 0.6
    return act(pos_goal, grab_effort, p=10)

@declare_tree('button-press-topdown')
def button_press_topdown(o_d):
    pos_curr = o_d['hand_pos']
    pos_button = o_d['obj1_pos']

    if jnp.linalg.norm(pos_curr[:2] - pos_button[:2]) > 0.04:
        return "put gripper above button"
    else:
        return "push down on button"

@declare_controller('button-press-topdown', "put gripper above button")
def gripper_above_button(o_d):
    return act(o_d['obj1_pos'] + jnp.array([0., 0., 0.1]), 1., p=25)

@declare_controller('button-press-topdown', "push down on button")
def push_down_on_button(o_d):
    return act(o_d['obj1_pos'], 1., p=25)

@declare_tree('pick-place')
def pick_place(o_d):
    pos_curr = o_d['hand_pos']
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    pos_goal = o_d['goal_pos']
    gripper_separation = o_d['gripper_distance_apart']
    # If error in the XY plane is greater than 0.02, place end effector above the puck
    if jnp.linalg.norm(pos_curr[:2] - pos_puck[:2]) > 0.02:
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

@declare_controller('pick-place', "place gripper above puck")
def place_gripper_above_puck(o_d):
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    return act(pos_puck + jnp.array([0., 0., 0.1]), 0., p=10)

@declare_controller('pick-place', "drop gripper around puck")
def drop_gripper_argound_puck(o_d):
    pos_puck = o_d['obj1_pos'] + jnp.array([-0.005, 0, 0])
    return act(pos_puck + jnp.array([0., 0., 0.03]), 0., p=10)

@declare_controller('pick-place', "close gripper around puck")
def close_gripper_around_puck(o_d):
    return act(o_d['hand_pos'], 1., p=10)

@declare_controller('pick-place', "place puck at goal")
def place_goal_at_puck(o_d):
    return act(o_d['goal_pos'], 1., p=10)

def parse_obs(obs):
    return {
        'hand_pos': obs[:3],
        'gripper_distance_apart': obs[3],
        'obj1_pos': obs[4:7],
        'obj1_rot': obs[7:11],
        'obj2_pos': obs[11:14],
        'obj2_rot': obs[14:18],
        'last_hand_pos': obs[18:21],
        'last_gripper': obs[21],
        'last_obj1_pos': obs[22:25],
        'last_obj1_rot': obs[25:29],
        'last_obj2_pos': obs[29:32],
        'last_obj2_rot': obs[32:36],
        'goal_pos': obs[36:39],
    }

def run_controller(controller_name, parsed_obs):
    controller_func = CONTROLLERS[controller_name]['function']
    controller_params = controller_func(parsed_obs)
    delta_xyz = move(parsed_obs['hand_pos'],
                     controller_params['target_xyz'],
                     controller_params['control_coeff'])

    return jnp.concatenate([delta_xyz, jnp.array([controller_params['grab_effort']])])


@dataclass
class SawyerUniversalV2Policy:

    env_name: str or None = None

    def get_action(self, obs):
        o_d = parse_obs(obs)
        tree = DECISION_TREES[self.env_name]['function']
        controller_name = tree(o_d)
        return run_controller(controller_name, o_d)

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

    for t, (r, done, info) in enumerate(trajectory_generator(env, policy, act_noise_pct, render)):
        rewards.append(r)
        assert not env.isV2 or set(info.keys()) == {
            'success',
            'near_object',
            'grasp_success',
            'grasp_reward',
            'in_place_reward',
            'obj_to_target',
            'unscaled_reward'
        }
        success |= bool(info['success'])
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
        a = policy.get_action(o)
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
    'env_name',
    MT10_V2.keys(),
)
@pytest.mark.parametrize('act_noise_pct', [0., 0.01, 0.05])
def test_universal_scripted_policy(env_name, act_noise_pct, iters=100):
    env = make_env(env_name)
    policy = SawyerUniversalV2Policy(env_name=env_name[:-3])

    successes = 0
    for _ in range(iters):
        successes += float(trajectory_summary(env, policy, act_noise_pct, render=False)[0])
    print(successes)
    expected_success_rate = 0.8
    assert successes >= expected_success_rate * iters
