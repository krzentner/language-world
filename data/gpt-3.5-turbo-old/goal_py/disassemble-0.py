# Steps:
#  1. Put gripper above the peg
#  2. Grab the wrench with the gripper
#  3. Pull the wrench off the peg
# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with the peg"):
    robot.move_gripper("vertically aligned with the peg")
# If the wrench isn't yet grabbed, grab it by closing the gripper.
if check("the robot's gripper is above the peg and the gripper is open"):
    robot.move_gripper("around the wrench", close_gripper=True)
# Once the wrench is grabbed, pull it off the peg.
if check("the wrench is grabbed by the gripper"):
    robot.move_gripper("above the peg")