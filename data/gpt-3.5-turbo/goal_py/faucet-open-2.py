# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle left to open the faucet
    # First, put the gripper roughly around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, we can try to turn the handle left
    # to open the faucet.
    # We can assume that if the gripper is around the handle, it is lined up with
    # the direction we want to turn the handle.
    if check("the robot's gripper is around faucet handle"):
        robot.turn_handle_left()