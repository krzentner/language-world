# Steps:
    #  1. Put gripper on faucet handle
    #  2. Turn the handle left
    # First, move the gripper onto the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # If the gripper is around the faucet handle, we can turn the handle left to
    # open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper on faucet handle
    #  2. Turn the handle right
    # First, move the gripper onto the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # If the gripper is around the faucet handle, we can turn the handle right to
    # close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle right")