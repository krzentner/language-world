

Then fill in code below it to implement `shelf-place`.

You do not need to fill in the docstring, only the main program
for `shelf-place`.
"""

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the block to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal")


print('Your code has been submitted.')
[eod] [code]import os
import numpy as np
import pandas as pd

# For Python2.x and Python3.x code compatible
try:
    input = raw_input
except NameError:
    pass

DATA_PATH = os.path.join("data", "churn.csv")


def is_float(str):
    try:
        float(str)
        return True
    except:
        return False


def data_check(data_array):
    """Checks if a data row is all filled.

    :param data_array: Data row (list/tuple)
    :return: