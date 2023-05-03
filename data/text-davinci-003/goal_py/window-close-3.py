
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the robot's gripper is near the window hanlde, we can slide the window
    # closed by pushing, so move the gripper right.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("horizontally aligned with the window handle")