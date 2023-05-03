
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle
    #  3. Pull the handle up
    # Put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, grab it.
    # We don't need to be careful about the direction here, since the handle is
    # narrow and we're grabbing it (unlike when pushing it).
    if check("the robot's gripper is not around handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # When the gripper is around the handle, we can just pull the handle up.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the door handle")