# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put the gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is not aligned with the gripper as seen from in front, we
    # should move the gripper in front of the drawer handle to pull the drawer.
    if check("the drawer handle is not forward aligned with the robot's gripper"):
        robot.move("gripper to front of drawer handle")
    # If the gripper is in front of the drawer handle, pull the drawer open.
    if check("the robot's gripper is in front of the drawer handle"):
        robot.pull("drawer open")