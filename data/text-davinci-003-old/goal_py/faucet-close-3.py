
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Start to turn the faucet right
    #  3. Turn the faucet harder
    # If the robot's gripper is not in front of the faucet handle, move the
    # gripper near the faucet handle.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the robot's gripper is near the faucet handle, start to turn the faucet.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # turn the faucet harder.
    if check("the robot's gripper is forward aligned with the faucet handle"):
        robot.move_gripper("right of the faucet handle")