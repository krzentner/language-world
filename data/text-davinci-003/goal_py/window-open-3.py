
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Pull the window open harder
    # If we're not at the window handle yet, move the gripper to the window
    # handle.
    if check("the robot's gripper is not left of the window handle"):
        robot.move_gripper("left of the window handle")
    # Once the robot's gripper is near the window handle, start pushing it
    # open.
    if check("the robot's gripper is near the window handle and the window handle is left of the robot's gripper"):
        robot.move_gripper("around the window handle")
    # If the gripper is around the window handle and the window is still closed,
    # press harder with the gripper.
    if check("the window handle is left of the robot's gripper"):
        robot.move_gripper("vertically aligned with the window handle")