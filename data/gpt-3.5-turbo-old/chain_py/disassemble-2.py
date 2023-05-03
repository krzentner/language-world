# Steps:
#  1. Put gripper above wrench
#  2. Grab the wrench with gripper
#  3. Pull the wrench off the peg
# First, put the gripper above the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.place("gripper above wrench")
# If the gripper is not already around the wrench, grab the wrench with the
# gripper.
if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
    robot.grab("the wrench")
# If the gripper is already around the wrench, pull the wrench off the peg.
if check("the robot's gripper is around the wrench and the wrench is fixed to the peg"):
    robot.pull("the wrench off the peg")