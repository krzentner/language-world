# Steps:
#  1. Put the gripper above the wrench
#  2. Grab the wrench with the gripper
#  3. Pull the wrench off the peg
# First, put the gripper above the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.put("gripper above wrench")
# If the gripper is above the wrench, grab it.
if check("the robot's gripper is above the wrench and the gripper is open"):
    robot.grab("wrench")
# If the gripper has successfully grabbed the wrench, pull it off the peg.
if check("the wrench is firmly in the gripper"):
    robot.pull("off the peg")