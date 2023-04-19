# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle but not to the right of it, move it to the right.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # Push against the window handle to start opening the window.
    if check("the robot's gripper is right of the window handle and the window is not fully open"):
        robot.move_gripper("vertically aligned with the window handle")
    # Push harder against the window handle to open it more.
    if check("the robot's gripper is forward aligned with the window handle and the window is not fully open"):
        robot.move_gripper("left of the window handle")