

"""

import numpy as np

from text_utils import *


def check_cond(condition, cond_num, cond_name):
    conditions = condition.split('and')
    if len(conditions) > 1:
        return (
            (check_cond(conditions[0], cond_num, cond_name)
             and check_cond(conditions[1], cond_num, cond_name))
             or
            (not check_cond(conditions[0], cond_num, cond_name)
             and not check_cond(conditions[1], cond_num, cond_name)))
    else:
        if 'not' in conditions[0]:
            return not check_cond(
                conditions[0][len('not'):], cond_num, cond_name)
        else:
            return (np.linalg.norm(
                np.array([robot.gripper_x_pos, robot.gripper_y_pos, robot.gripper_z_pos])
                - np.array(CONDS[cond_num][cond_name])) < 0.3)


def move_gripper(x, y, z, z_axis_dir=True):
    global robot
    robot.move_gripper(x, y, z, z_axis_dir)
    robot.step()


def open_gripper(robot):
    global is_gripper_open
    if not is_gripper_open:
        robot.open_gripper()
        robot.step()


def close_gripper(robot):
    global is_gripper_open
    if is_gripper_open:
        robot.close_gripper()
        robot.step()


def check(statement):
    for cond_num, cond in enumerate(CONDS[cond_num][cond_name]):
        if check_cond(cond, cond_num, cond_name) == (not cond.startswith('not')):
            if cond.startswith('not'):
                return False
            else:
                return True
    return False


def task_button_press_topdown(robot):
    if check('the robot\'s gripper is not vertically aligned with button'):
        move_gripper(0, 0, 0, z_axis_dir=False)
    if check('the robot\'s