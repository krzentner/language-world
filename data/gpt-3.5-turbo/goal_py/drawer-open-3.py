# Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    #  3. Put gripper back to starting position
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    # We need to be careful about the direction, since we might bump into the
    # drawer if we're not aligned right.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle", close_gripper=True)
    # If the drawer handle is aligned with the gripper as seen from in front, we
    # can push the drawer open. We also need to make sure the gripper doesn't
    # bump into the front of the drawer while pulling it.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")
        robot.move_gripper("vertically aligned with the drawer handle", close_gripper=False)