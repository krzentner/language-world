
    # Steps:
    #  1. Line up the gripper as seen from the side
    #  2. Turn the handle to the left
    # Because this is a "turn" task, the robot's gripper should be aligned with
    # the handle as seen from the side. This is because we want to move the
    # handle around its axel, not push or pull it.
    # If the robot's gripper is not left of the faucet as seen from the side,
    # move the gripper.
    if check("the robot's gripper is not left of the faucet"):
        robot.move_gripper("left of the faucet")
    # If the gripper is left of the faucet, try to turn the faucet handle.
    if check("the robot's gripper is left of the faucet"):
        robot.move_gripper("horizontally aligned with the faucet")