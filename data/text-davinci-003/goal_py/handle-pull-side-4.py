
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # If the gripper isn't near the handle, drop it near the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("near the handle")
    # Use the same check from above to make sure the handle is still below the
    # gripper before pulling.
    if check("the robot's gripper is near handle and the robot's gripper is closed"):
        robot.move_gripper("upward aligned with the handle")