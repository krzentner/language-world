# Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet right to close
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper isn't around the faucet handle, put it around the handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, turn the handle to the right
    if check("the robot's gripper is around faucet handle"):
        robot.turn_handle("right")