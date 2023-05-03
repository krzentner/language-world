# Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We need to be a bit more careful about the direction when opening the
    # drawer, so we'll use a different check condition than when closing it.
    if check("the robot's gripper is not behind the drawer handle"):
        robot.grab("drawer handle from behind")
    # As long as the gripper is behind the drawer handle, it's being opened, so
    # keep pulling.
    if check("the robot's gripper is behind the drawer handle"):
        robot.pull("drawer open")