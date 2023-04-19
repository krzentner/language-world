# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle right
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper is around the handle, we can turn it right to close the
    # faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned right")