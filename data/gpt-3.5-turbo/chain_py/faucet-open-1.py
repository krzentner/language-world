# Steps:
#  1. Put gripper around the faucet handle
#  2. Twist the handle left to open the faucet
# First, put the gripper around the faucet handle.
if check("the robot's gripper is not around the faucet handle"):
    robot.drop("gripper around faucet handle")
# Once the gripper is around the handle, we can turn it left to open the
# faucet.
if check("the robot's gripper is around the faucet handle"):
    robot.twist("handle left to open faucet")