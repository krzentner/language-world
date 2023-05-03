# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle to the right
    # If the handle isn't already around the robot's gripper, move the gripper
    # around it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the handle is around the gripper and is turned left of the closed position,
    # turn it to the right.
    if check("the robot's gripper is around the faucet handle and the faucet is not closed"):
        robot.move_gripper("turn the handle to the right")