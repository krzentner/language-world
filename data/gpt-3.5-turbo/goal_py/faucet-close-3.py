# Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet handle right to close
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper not around the faucet handle, put it around.
    if check("the robot's gripper is not around the faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, turn the handle right to close.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turn the faucet handle right")