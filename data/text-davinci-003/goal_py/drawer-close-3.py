
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Start pushing against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # We just need to move the gripper left of the drawer handle to start pushing
    # it.
    if check("the robot's gripper is right of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # If the robot's gripper is getting near the drawer handle, we can push the
    # drawer closed.
    if check("the robot's gripper is almost right of the drawer handle and the robot's gripper is almost near drawer handle"):
        robot.move_gripper("right of the drawer handle")
    # If the gripper is near the drawer handle, push harder.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("left of the drawer handle")