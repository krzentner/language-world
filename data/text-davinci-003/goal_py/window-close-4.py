
    # Steps:
    #  1. Put gripper near the window handle
    #  2. Push the window back to the right
    # To close the window, we need to move the gripper near the window handle.
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # Now that the gripper is near the window handle, we can start pushing against it to close the window.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("above the window handle")