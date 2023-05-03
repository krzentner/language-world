
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not aligned to the window handle, we should
    # move the gripper near the window handle to start closing the window
    if check("the robot's gripper is above the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed by pushing the gripper right. We should close the gripper
    # so it gets a good grip on the window handle.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle", close_gripper=True)