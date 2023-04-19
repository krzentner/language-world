# window-open: slide the window open to the left
# def window_open(robot):
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
        robot.move_gripper("left of the window handle", close_gripper=True)
    # If the gripper is around the window handle and the window isn't completely
    # open, keep pushing.
    if check("the robot's gripper is around the window handle and the window is not completely open"):
        robot.move_gripper("left of the window handle")