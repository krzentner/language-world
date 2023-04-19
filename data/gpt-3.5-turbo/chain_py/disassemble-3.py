# Steps:
#  1. Put gripper above the wrench
#  2. Grab the wrench with the gripper
#  3. Pull the wrench off the peg
# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with the wrench"):
    robot.put("gripper above wrench")
# If the gripper is above the wrench, grab the wrench.
if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around wrench"):
    robot.grab("wrench")
# If the wrench is free from the peg, assume it's been disassembled. Otherwise,
# pull the wrench off the peg.
if check("the wrench is not free from the peg"):
    robot.pull("wrench off peg")