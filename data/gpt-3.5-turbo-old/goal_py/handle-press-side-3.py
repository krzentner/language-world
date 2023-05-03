# Steps:
# 1. Put gripper near the handle
# 2. Move the gripper towards the handle until it's pushing down on the handle
# Because this is "side", we just need to put the gripper near the handle and
# then move it towards the handle until it's pushing down on the handle.
# First, put the gripper near the handle.
if check("the robot's gripper is not near the handle"):
    robot.move_gripper("near the handle")
# Then, move the gripper towards the handle until it's pushing down on the handle.
if check("the robot's gripper is not pushing down on the handle"):
    robot.move_gripper("pushing down on the handle")