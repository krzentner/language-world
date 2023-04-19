# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the faucet right
    # First, put the gripper around the faucet handle
    if check("the robot's gripper is not around faucet handle"):
        robot.drop("the gripper around faucet handle")
    # Then, turn the faucet handle right
    if check("the robot's gripper is around faucet handle and faucet handle is not turned right"):
        robot.turn("faucet handle right")