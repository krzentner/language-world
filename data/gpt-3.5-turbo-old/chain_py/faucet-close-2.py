# Steps:
    #  1. Align the gripper with the faucet handle
    #  2. Turn the faucet right to close it
    # Align the robot's gripper with the faucet handle.
    if check("the robot's gripper is not aligning with the faucet handle"):
        robot.align("gripper with faucet handle")
    # Turn the faucet handle right to close it.
    if check("the robot's gripper is aligned with the faucet handle"):
        robot.turn("faucet right to close it")