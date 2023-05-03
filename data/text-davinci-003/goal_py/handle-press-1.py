
    # Steps:
    #  1. Put gripper near handle
    #  2. Push down the handle
    # We need to move the gripper near the handle before we can push it.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Now that the gripper is near the handle, we can then push down the handle.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("around the handle")