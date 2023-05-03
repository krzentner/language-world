
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the gripper is not vertically aligned with the window handle, move the
    # gripper to the side of the window handle.
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the window handle is right of the robot's gripper, we should move the
    # gripper right of the window handle to start pushing.
    if check("the window handle is right of the robot's gripper"):
        robot.move_gripper("left of the window handle")
    # Once the robot's gripper has progressed past the window handle, push
    # harder to slide the window open.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("left of the window handle")