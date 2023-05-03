
    # Steps:
    #  1. Line up the gripper with the handle
    #  2. Push down on the handle
    # Because we don't need to open the handle, we just need to line up the
    # gripper from above.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")