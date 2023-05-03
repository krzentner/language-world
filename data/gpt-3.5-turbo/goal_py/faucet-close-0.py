# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the faucet right to close it
    # To close the faucet, we need to grab the handle and turn it to the right.
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # If the gripper is around the handle, turn the handle to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned to the right")