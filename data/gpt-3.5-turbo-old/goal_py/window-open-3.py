# Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is right of the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle", close_gripper=True)
    # If the gripper is already almost lined up with the window handle, push the window open harder.
    # Use the gripper's force sensor to detect when we're pushing against the window handle hard enough.
    if check("the robot's gripper is almost vertically aligned with the window handle and exerting enough force to push the window open"):
        robot.move_gripper("horizontally aligned with the left edge of the window")