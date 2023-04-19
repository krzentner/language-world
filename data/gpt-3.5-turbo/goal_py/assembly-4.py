# Steps:
#  1. Put gripper above the wrench and peg
#  2. Grab the wrench with the gripper
#  3. Place the wrench around the peg
# First, put the robot's gripper above the wrench and peg.
if check("the robot's gripper is not vertically aligned with the wrench and peg"):
    robot.move_gripper("vertically aligned with the wrench and peg")
# Grab the wrench with the gripper.
if check("the robot's gripper is not around the wrench and peg"):
    robot.move_gripper("around the wrench and peg", close_gripper=True)
# Place the wrench around the peg.
if check("the wrench is not around the peg and the gripper is aligned with the peg"):
    robot.move_gripper("around the peg")