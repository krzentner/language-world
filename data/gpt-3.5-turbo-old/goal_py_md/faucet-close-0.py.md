# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put the gripper left of the faucet handle
    #  2. Grab the faucet handle
    #  3. Turn the handle right to close the faucet
    # First, put the gripper left of the faucet handle.
    if check("the robot's gripper is not left of the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the gripper is near the faucet handle, grab it.
    if check("the robot's gripper is near the faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper is around the faucet handle, turn the handle right to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle")