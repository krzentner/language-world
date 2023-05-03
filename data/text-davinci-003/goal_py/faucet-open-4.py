
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Push gripper into top of faucet handle
    #  3. Rotate faucet handle left
    # If the gripper is not above the faucet handle, place it above the faucet
    # handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Once the gripper is lined up above the faucet handle, the robot should
    # close the gripper to trap the handle and then rotate it to the left.
    # Once the gripper is around the faucet handle, close the gripper to trap it.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.move_gripper("above the faucet handle", close_gripper=True)
    # If the gripper is around the handle, rotate it as far as possible to the
    # left.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the faucet handle")