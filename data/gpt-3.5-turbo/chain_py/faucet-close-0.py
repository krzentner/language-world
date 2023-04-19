# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn handle to the right to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.drop("gripper around faucet handle")
    # Turn the faucet handle to the right to close it.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet handle to the right")