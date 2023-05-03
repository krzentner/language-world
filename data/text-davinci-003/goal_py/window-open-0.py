
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # Put the robot's gripper left of the window handle.
    if check("the robot's gripper is not left of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is near the window handle, we should be able to
    # start pushing against it.
    if check("the robot's gripper is left of the window handle and the robot's gripper is not almost vertically aligned with window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the gripper is starting to move the window handle, the window should be
    # opening. Push the gripper harder.
    if check("the robot's gripper is almost vertically aligned with window handle"):
        robot.move_gripper("forward aligned with the window handle")