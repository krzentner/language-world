# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle left
    #  3. Open faucet more
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Turn the handle to the left to start opening the faucet.
    if check("the robot's gripper is around the faucet handle and the faucet is not open"):
        robot.move_gripper("left of the faucet handle")
    # If the handle has started to turn left, keep turning it left to open the
    # faucet more.
    if check("the faucet is not fully open"):
        robot.move_gripper("left of the faucet handle")