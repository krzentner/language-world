

Once you're finished, click the "Check" button.
'''


# YOUR CODE GOES HERE.

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):


# Steps:
#  1. Put the gripper above the peg in the hole
#  2. Grab the peg out of the hole
#  3. Move the peg to the target location

# If the gripper is not directly above the peg, we need to start from the beginning.
# Since the peg is in the hole, we can check if the gripper is above both.
if check("the robot's gripper is not above the peg and the robot's gripper is not above the hole"):
    robot.move_gripper("vertically aligned with the peg in the hole")

# As long as the gripper is lined up with the hole, we can grab the peg out of the hole.
if check("the robot's gripper is above the peg"):
    robot.move_gripper("below the hole", close_gripper=True)

# If the gripper is closed, open it. We don't need to grab the peg.
if check("the robot's gripper is above the peg and the robot's gripper is closed"):
    robot.move_gripper("open the robot's gripper")

# Once the gripper is closed around the peg, we can pick it up out of the hole.
if check("the robot's gripper is above the peg and the robot's gripper is closed"):
    robot.move_gripper("up from the hole")

# Now that the peg is out of the hole, we can move the gripper to the target location.
if check("the peg is not in the hole"):
    robot.move_gripper("vertically aligned with the target location")

# Now that the peg is at the target location, we can drop it.
if check("the robot's gripper is above the peg"):
    robot.move_gripper("above the target location", open_gripper=True)
[eod] [code]import os
import re

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class ImageUtil:
    """
    Class containing functions for processing images
    """

    def __init__(self, args):
        self.args = args
        self.input_dir = os.path.join(args.data