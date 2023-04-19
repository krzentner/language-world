# window-close: slide the window closed to the right
# def window_close(robot):
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle", close_gripper=True)
    # After the gripper is close, we can slide the window close by moving the
    # gripper to the right.
    if check("the robot's gripper is almost aligned with the window frame"):
        robot.move_gripper("right of the window frame")