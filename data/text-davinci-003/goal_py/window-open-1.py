
    # Steps:
    #  1. Put gripper slightly above window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # We need to be careful here because the window could break if we push too
    # hard.
    # First, put the robot's gripper slightly above the window handle.
    if check("the robot's gripper is not above the window handle"):
        robot.move_gripper("above the window handle")
    # Once the gripper is mostly above the window handle, we can carefully push
    # the window open with the gripper.
    if check("the robot's gripper is almost vertically aligned with the window handle"):
        robot.move_gripper("right of the window handle")
    # Carefully push the window open harder, if the gripper is right of the
    # window handle.
    if check("the window handle is right of the robot's gripper"):
        robot.move_gripper("forward aligned with the window handle")