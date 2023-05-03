
    # Steps:
    #  1. Put gripper near the faucet
    #  2. Turn the faucet to the left
    # We need to start with the gripper near the faucet.
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")
    # If the gripper is near the faucet, but the faucet hasn't been turned all
    # the way to the left, keep turning until it's there.
    if check("faucet is not fully left"):
        robot.move_gripper("left of the faucet")