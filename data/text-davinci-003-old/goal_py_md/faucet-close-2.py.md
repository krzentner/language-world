

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet right to close it
    # First, put the gripper roughly above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper isn't around the faucet handle, put it around the handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the gripper is near the faucet handle, turn the faucet right to close it.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("right of the faucet handle")