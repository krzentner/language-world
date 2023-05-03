# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle right to close the faucet
    # We need to grab the faucet handle before we can turn it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper is around the handle, we can turn it to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("facing the right direction")