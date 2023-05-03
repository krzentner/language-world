
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # First, put the gripper sideways to the window handle to start pushing
    # against it.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle and still sideways to it,
    # we can start pushing it open.
    if check("the robot's gripper is right of the window handle and the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle and ahead of it, push
    # harder.
    if check("the robot's gripper is near the window handle and the robot's gripper is forward aligned with the window handle"):
        robot.move_gripper("forward aligned with the window handle")