
    # Steps:
    #  1. Put the gripper near the faucet handle
    #  2. Turn the faucet handle to the right
    # First, put the gripper near the faucet handle
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")
    # Now, turn the faucet handle to the right
    if check("the robot's gripper is near the faucet"):
        robot.move_gripper("right of the faucet")