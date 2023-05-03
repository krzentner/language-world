
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Starting turning the handle right
    #  3. Turn the handle right harder
    # The robot needs to line up with the handle differently when it's open and
    # when it's closed, so if it's closed, move the gripper left of the handle.
    if check("the robot's gripper is not left of faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # Once the gripper is left of the handle, try to turn the handle right.
    if check("the robot's gripper is left of faucet handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the faucet handle")
    # If the handle is to the right of the robot's gripper, push on it harder to
    # make it close.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")