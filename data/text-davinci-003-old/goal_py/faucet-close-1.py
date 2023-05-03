
    # Steps:
    #  1. Put gripper left of the faucet
    #  2. Push against the faucet
    #  3. Turn the faucet to the right
    # First, put the gripper slightly left of the faucet so that we can push it.
    if check("the robot's gripper is not left of the faucet"):
        robot.move_gripper("left of the faucet")
    # If the gripper is far left of the faucet, move it closer.
    if check("the robot's gripper is near the faucet and the faucet is not right of the robot's gripper"):
        robot.move_gripper("right of the faucet", close_gripper=True)
    # If the faucet is right of the robot's gripper, go ahead and start pushing.
    if check("the faucet is right of the robot's gripper"):
        robot.move_gripper("forward aligned with the faucet")