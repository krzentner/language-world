# Steps:
    #  1. Put gripper behind the drawer handle
    #  2. Push the drawer closed
    # If the robot's gripper is not behind the drawer handle, we need to move it
    # there before we can push the drawer closed.
    if check("the robot's gripper is not behind the drawer handle"):
        robot.move_gripper("behind the drawer handle")
    # Now that the gripper is behind the drawer handle, we can just push the
    # drawer closed by moving the gripper forward.
    if check("the robot's gripper is behind the drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")