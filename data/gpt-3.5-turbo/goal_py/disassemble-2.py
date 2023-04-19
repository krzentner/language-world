# Steps:
#  1. Put gripper near the wrench handle
#  2. Grab the wrench handle with the gripper
#  3. Pull the wrench off the peg
# First, put the gripper near the wrench handle.
if check("the robot's gripper is not near the wrench handle"):
    robot.move_gripper("near the wrench handle")
# If the gripper is near the wrench handle, grab it.
if check("the robot's gripper is near the wrench handle and the gripper is not closed"):
    robot.move_gripper("around the wrench handle")
# If the wrench is grabbed by the gripper, pull it off the peg.
if check("the wrench is grabbed by the gripper"):
    robot.move_gripper("away from the peg")