# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    # 1. Put the gripper around the handle
    # 2. Turn the handle right to close the faucet
    # First, put the gripper around the handle
    if check("the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # If the gripper is around the handle, turn the handle right to close the faucet
    if check("the robot's gripper is around faucet handle and the handle is not turned right"):
        robot.move_gripper("turning the handle right")