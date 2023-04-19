
    # Steps:
    #  1. Align the gripper with the faucet handle from behind
    #  2. Grab the handle by closing the gripper
    #  3. Turn the handle to the right to close the faucet
    # First, line up the gripper with the faucet handle from behind.
    if check("the robot's gripper is not behind aligned with faucet handle"):
        robot.move_gripper("behind aligned with the faucet handle", close_gripper=True)
    # Once the gripper is partially around the faucet handle, close the gripper
    # to grab it.
    if check("the robot's gripper is behind aligned faucet handle"):
        robot.move_gripper("near the faucet handle")
    # Now that the faucet handle is gripped, turn it to the right to close the
    # faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("clockwise aligned with faucet handle")