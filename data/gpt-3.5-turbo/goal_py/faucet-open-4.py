# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle left to open faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn the handle left to open
    # the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned to the left")