# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle isn't lined up with the gripper, put the gripper around the
    # handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Now that the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the bottom of the handle")