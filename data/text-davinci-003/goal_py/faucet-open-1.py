
    # Steps:
    #  1. Put gripper below the faucet handle
    #  2. Reach up and grab the faucet handle from below
    #  3. Turn the faucet handle left
    # We should start by putting the gripper below the faucet handle, since the
    # robot can't grab from above.
    if check("the robot's gripper is not below the faucet handle"):
        robot.move_gripper("below the faucet handle")
    # If the gripper is below the faucet handle but not near it, move it closer
    # to the faucet handle.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("above the faucet handle", close_gripper=True)
    # If the gripper is near the faucet handle, we can turn the faucet to the
    # left.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("left of the faucet handle")