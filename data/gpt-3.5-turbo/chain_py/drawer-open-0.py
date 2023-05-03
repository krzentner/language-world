# Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We need to be careful about the direction since the drawer is large and
    # we need to pull it towards us to open it (unlike when closing the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the gripper is behind the drawer handle and the drawer is closed, pull
    # it open.
    if check("the robot's gripper is behind drawer handle and the drawer is closed"):
        robot.pull("the drawer open")