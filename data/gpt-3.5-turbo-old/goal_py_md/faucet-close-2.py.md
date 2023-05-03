# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn handle to the right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Once the gripper is above the faucet handle, put it around the handle.
    if check("the robot's gripper is not around faucet handle" and "the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, turn it to the right by moving it
    # to the right.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("turned right")