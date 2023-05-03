# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle, being careful not to pull the drawer closed while we're doing so.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move("gripper to approximately above drawer handle")
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pulling it.
    if check("the robot's gripper is above drawer handle"):
        robot.pull("drawer open")