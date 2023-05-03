# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle left to open the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the handle, turn it left to open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle right to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the handle, turn it right to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle right")