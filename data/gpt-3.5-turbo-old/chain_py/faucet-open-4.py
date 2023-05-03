# Steps:
#  1. Put gripper around faucet handle
#  2. Turn the handle left to open the faucet
# First, put the gripper around the faucet handle.
if check("the robot's gripper is not around the faucet handle"):
    robot.drop("gripper around faucet handle")
# If the handle isn't turned all the way left, turn it left to open the faucet.
if check("the faucet handle is not turned all the way left"):
    robot.turn_left("faucet handle")