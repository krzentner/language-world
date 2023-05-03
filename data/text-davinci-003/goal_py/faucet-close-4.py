
    # Steps:
    #  1. Put gripper above faucet
    #  2. Push faucet to the right
    # First, put the gripper above the faucet.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.move_gripper("vertically aligned with the faucet", close_gripper=True)
    # Now that the gripper is lined up, just push the faucet to the right.
    if check("the robot's gripper is vertically aligned with the faucet"):
        robot.move_gripper("right of the faucet")