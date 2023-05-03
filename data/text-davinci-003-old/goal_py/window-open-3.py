
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not right of the window handle, we should move
    # the gripper to the right of the window handle.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle, start pushing to open it.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the window handle is starting to move, push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("left of the window handle")