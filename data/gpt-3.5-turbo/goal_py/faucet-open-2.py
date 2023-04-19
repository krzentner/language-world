# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle to the left to open the faucet
    # To open the faucet, we need to get the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the handle, we can turn it left to open the
    # faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned left")