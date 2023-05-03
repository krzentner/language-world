
    # Steps:
    #  1. Put gripper forward of drawer handle
    #  2. Start pushing against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # First, put the gripper in front of the drawer handle so we can start
    # pushing against it.
    if check("the robot's gripper is not forward aligned with the drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle")
    # If the gripper is near the drawer handle, we can just push harder,
    # allowing the robot to close the drawer.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("right of the drawer handle")