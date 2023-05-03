# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle clockwise to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the handle, turn it clockwise to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turning the handle clockwise")