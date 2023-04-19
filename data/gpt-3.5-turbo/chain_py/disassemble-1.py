# Steps:
#  1. Put gripper above the wrench
#  2. Grab the wrench with the gripper
#  3. Pull the wrench off the peg
# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with the wrench"):
    robot.put("gripper above wrench")
# Once the gripper is above the wrench, grab it.
if check("the robot's gripper is almost vertically aligned with the wrench and the robot's gripper is open"):
    robot.grab("wrench")
# Once the wrench is grabbed, pull it off the peg.
if check("the wrench is grabbed by the gripper"):
    robot.pull("wrench off peg")