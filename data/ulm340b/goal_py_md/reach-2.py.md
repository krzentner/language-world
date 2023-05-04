

In addition to the function name, the first line must be a description of the task in the form `# <task-name>: <description>`.
Your description will be used to explain to other programmers what the function does.

For the task, the robot's goal is to reach out its gripper and touch the target.

This is a tricky function to write, and it's okay if your code doesn't always work.
"""

import math
import utils
import utils_robot


# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole to the side, insert it.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    #