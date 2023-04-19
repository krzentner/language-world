# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper near the faucet handle
    #  2. Turn the handle right
    # First, put the gripper near the faucet handle.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # If the gripper is near the faucet handle, turn the handle right.
    if check("the robot's gripper is near the faucet handle and the handle is not turned right"):
        robot.move_gripper("around the faucet handle to the right")