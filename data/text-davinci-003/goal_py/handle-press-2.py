
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle
    # Again, the robot should fully line up the gripper from above before
    # interacting with the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")