
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # We need robot gripper on the right side of the window handle in order to
    # begin pushing it.
    if check("the robot's gripper is not on the right side of the window handle"):
        robot.put("gripper beside window handle")
    # Now that the gripper is positioned correctly, we can start pushing.
    if check("the robot's gripper is on the right side of the window handle"):
        robot.push("window handle")
    # If the window handle is unlocked, continue pushing the window open.
    if check("the window handle is unlocked"):
        robot.push("window open harder")