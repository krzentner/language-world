

Steps:
1. Put gripper right of the window handle
2. Start pushing against the window handle to open the window
3. Push the window open harder

	if check("the window handle is left of the robot's gripper"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is not near the window handle and the window handle is right of the robot's gripper"):
        robot.move_gripper("around the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("horizontally aligned with the window handle")