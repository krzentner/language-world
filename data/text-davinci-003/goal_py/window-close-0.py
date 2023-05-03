
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Push the window towards the center
    #  3. Push the window closed harder
    # We should move the gripper near the window handle to start pushing.
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the window handle is left of the gripper, it's probably lined up and
    # we can start pushing.
    if check("the window handle is left of the gripper"):
        robot.move_gripper("forward aligned with the window handle")
    # If the gripper is lined up with the window handle, push harder and keep
    # pushing until the window is closed.
    if check("the robot's gripper is forward aligned with the window handle"):
        robot.move_gripper("behind the window handle")