# Steps:
#  1. Put gripper above the wrench
#  2. Grab the wrench with the gripper
#  3. Pull the wrench off the peg
#  4. Drop the wrench
# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with the wrench"):
    robot.move_gripper("vertically aligned with the wrench")
# If the wrench isn't grabbed by the gripper, grab it.
if check("the robot's gripper is not around the wrench"):
    robot.move_gripper("around the wrench")
# Once the wrench is grabbed by the gripper, pull it off the peg by moving the
# gripper upwards.
if check("the wrench is on the peg and the robot's gripper is around the wrench"):
    robot.move_gripper("above the peg")
# Once the wrench is off the peg, drop it.
if check("the robot's gripper is above the peg and the wrench is in the gripper"):
    robot.move_gripper("above the drop location", open_gripper=True)