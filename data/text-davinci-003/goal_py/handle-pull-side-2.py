
    # Steps:
    #  1. Put gripper on the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    # First, we need to put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # As long as the handle isn't pulled up, line up the gripper with the handle
    # from the side.
    if check("the handle is not upright and the robot's gripper is not aligned with handle in the forward direction"):
        robot.move_gripper("forward aligned with handle")
    # If the handle is aligned with the gripper, pull the handle up.
    if check("the handle is not upright and the robot's gripper is almost vertically aligned with handle"):
        robot.move_gripper("upward aligned with handle")