# Steps:
    #  1. Put the gripper above the faucet handle
    #  2. Turn the handle right to close the faucet
    # First, put the gripper roughly above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is above the faucet handle, turn the handle right to
    # close the faucet.
    # We don't need to be careful about the direction, since the faucet handle
    # will only turn one way to close.
    if check("the robot's gripper is above the faucet handle"):
        robot.turn("faucet handle right to close")