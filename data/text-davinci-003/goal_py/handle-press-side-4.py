
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the handle from the side
    # We don't need to put the gripper above the handle for this, we just need to
    # be lined up with it from the side.
    if check("the robot's gripper is not side aligned with handle"):
        robot.move_gripper("side aligned with the handle")
    # Now that the gripper is lined up to the side, just push down on the handle.
    if check("the robot's gripper is side aligned with handle"):
        robot.move_gripper("near the handle")