
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is vertically aligned with the window handle and the robot's gripper is not near the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("forward aligned with the window handle")