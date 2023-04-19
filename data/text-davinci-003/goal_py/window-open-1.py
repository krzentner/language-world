
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # First, put the gripper near the window handle, as we will be pushing from
    # the side.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the the window handle is right of the robot's gripper, we can start
    # pushing by moving the gripper down.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not almost vertically aligned with window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is almost vertically aligned with the window handle"):
        robot.move_gripper("horizontally aligned with the