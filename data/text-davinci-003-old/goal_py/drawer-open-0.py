
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper roughly above the drawer handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not above the drawer handle"):
        robot.move_gripper("above the drawer handle")
    # If the gripper isn't around the drawer handle, put it around the drawer
    # handle.
    if check("the robot's gripper is not around drawer handle"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")