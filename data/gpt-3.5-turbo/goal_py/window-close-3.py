# Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not left of the window handle, we should move the
    # gripper left of the handle to start pushing.
    if check("the robot's gripper is not left of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the gripper is left of the handle, we can slide the window closed by
    # moving the gripper right.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")