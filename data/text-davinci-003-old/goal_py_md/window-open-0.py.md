

# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not right of the window handle, move the gripper
    # near the window handle to begin pushing.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle, we can probably slide
    # the window open now by moving the gripper left.
    if check("the robot's gripper is almost vertically aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the gripper is starting to be in front of the window handle, push
    # harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("left of the window handle")