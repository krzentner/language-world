
    # Steps:
    #  1. Put gripper around the drawer handle
    #  2. Pull the drawer open
    # First, carefully line up the robot's gripper with the drawer handle, so
    # that we don't bump the drawer while trying to open it.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # If the gripper is aligned, pull the drawer open.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.move_gripper("right of the drawer handle")