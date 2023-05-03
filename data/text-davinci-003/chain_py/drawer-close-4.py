
    # Steps:
    #  1. Put gripper right of the drawer handle
    #  2. Push against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # 
    #
    #
    # We need to put the gripper a bit to the side of the drawer handle before we
    # can push it, since the robot's grippher isn't perfectly straight.
    if check("the robot's gripper is not near drawer handle and the drawer handle is right of the robot's gripper"):
        robot.move("gripper to left of drawer handle")
    # Now that the robot's gripper is in the right spot, we can start pushing
    # the drawer closed.
    if check("the robot's gripper is near drawer handle"):
        robot.push("drawer closed")
    # If the drawer handle is getting in front of the robot's gripper, we need to
    # push harder.
    if check("the robot's gripper is in front of drawer handle"):
        robot.push("drawer closed harder")