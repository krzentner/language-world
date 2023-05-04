
    Steps:  1. Put gripper above the handle  2. Put the gripper around the handle  3. Lift the handle up
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with the handle, the robot should put gripper above handle.
    Once the gripper is lined up above the handle, we should be able to grab the handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle, the robot should put gripper around handle.
    Once the gripper is around the handle, we can just pull the handle up.
    - When the robot's gripper is around the handle, the robot should pull handle up.

The task `peg-unstack` requires the robot to slide the top peg off the bottom peg.
To slide the top peg off the bottom peg reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the handle  2. Put the gripper around the handle  3. Lift the handle up
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with the handle, the robot should put gripper above handle.
    Once the gripper is lined up above the handle, we should be able to grab the handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle, the robot should put gripper around handle.
    Once the gripper is around the handle, we can just pull the handle up.
    - When the robot's gripper is around the handle, the robot should pull handle up.
'''


def create_policy_for(task, domain, env, policy_factory, **kwargs):
    policy = policy_factory(**kwargs)
    domain = make_task(task)(domain)
    env = make_task(task)(env)
    domain.train(env, policy)
    return policy


def make_task(task):
    task = {
        'reach': make_reach,
        'push': make_push,
        'window-close': make_window_close,
        'window-open': make_window_open,
        'drawer-close': make_drawer_close,
        'button-press-topdown': make_button_press_topdown,
        'pick-place': make_pick_