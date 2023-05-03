# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle right to close the faucet
    # First, get the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the faucet handle, we need to turn it right to
    # close the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.rotate("faucet handle right to close faucet")