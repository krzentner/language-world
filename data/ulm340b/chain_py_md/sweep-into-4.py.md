

and fill in the steps necessary to perform the task.
Note that you're not limited to the methods used in the other tasks; feel free to be creative.
"""

import numpy as np

class CheckFailure(Exception):
    pass

def check(cond_str):
    if cond_str == "cube is above block":
        return check_robot_above(robot, cube)
    elif cond_str == "cube is on the ground":
        return check_on_ground(robot, cube)
    elif cond_str == "the robot's gripper is near the cube":
        return check_near(robot, cube)
    elif cond_str == "the robot's gripper is not near the cube":
        return not check_near(robot, cube)
    elif cond_str == "the robot's gripper is around the cube":
        return check_around(robot, cube)
    elif cond_str == "the robot's gripper is not around the cube":
        return not check_around(robot, cube)
    elif cond_str == "the robot's gripper is above cube":
        return check_above(robot, cube)
    elif cond_str == "the robot's gripper is not above cube":
        return not check_above(robot, cube)
    elif cond_str == "cube is in front of the robot's gripper":
        return check_in_front(robot, cube)
    elif cond_str == "cube is not in front of the robot's gripper":
        return not check_in_front(robot, cube)
    elif cond_str == "the robot's gripper is near block":
        return check_near(robot, block)
    elif cond_str == "the robot's gripper is not near block":
        return not check_near(robot, block)
    elif cond_str == "the robot's gripper is around block":
        return check_around(robot, block)
    elif cond_str == "the robot's gripper is not around block":
        return not check_around(robot, block)
    elif cond_str == "the robot's gripper is above block":
        return check_above(robot, block)
    elif cond_str == "the robot's gripper is not above block":
        return not check_above(robot, block)
    elif cond_str == "block is in front of the robot's gripper":
        return check_in_front(robot