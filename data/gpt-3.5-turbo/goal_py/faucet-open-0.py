# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle left
    # First, move the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn it left.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle right
    # First, move the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn it right.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned right")