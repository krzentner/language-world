
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # First, move the robot's gripper near the window handle.
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle, try to slide the window
    # closed by pushing it right.
    if check("the robot's gripper is forward aligned with the window handle"):
        robot.move_gripper("around the window handle")