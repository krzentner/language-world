# Steps:
#  1. Put gripper around faucet handle
#  2. Turn handle right to close faucet
# First, we need to put the gripper around the faucet handle.
if check("the robot's gripper is not around the faucet handle"):
    robot.move_gripper("around the faucet handle")
# Once the gripper is around the faucet handle, we can turn it right to close
# the faucet.
if check("the robot's gripper is around the faucet handle"):
    robot.move_gripper("horizontally aligned with the faucet handle")