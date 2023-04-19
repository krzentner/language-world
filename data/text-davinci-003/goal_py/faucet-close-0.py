
    # Steps:
    #  1. Put gripper near the faucet
    #  2. Turn the faucet right
    # First, put the gripper roughly near the faucet.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # As long as the gripper is close to the faucet handle, it should be able
    # to turn it.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("right of the faucet handle")