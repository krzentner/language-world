# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle right to close the faucet
    #  3. Keep turning if the faucet is not fully closed
    # First, position the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # If the gripper is around the handle, turn the handle to the right to close
    # the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn_right("faucet handle")
    # If the faucet is still not fully closed, keep turning.
    # We can check this by seeing if the robot's gripper is in front of the
    # faucet handle.
    while check("the robot's gripper is not in front of the faucet handle"):
        robot.turn_right("faucet handle")