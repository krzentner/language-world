# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pulling it (unlike when closing the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move("gripper to handle")
    # If the drawer handle is mostly above the gripper, closing it should line
    # it up all the way.
    if check("the drawer handle is mostly above the gripper and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # As long as the gripper is around the handle, it's being opened, so keep pulling.
    if check("the robot's gripper is around the handle"):
        robot.pull("drawer open")