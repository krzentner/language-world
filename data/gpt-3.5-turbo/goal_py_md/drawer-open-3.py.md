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
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("above the drawer handle")  # move gripper above the handle
        robot.move_gripper("above the drawer")  # move gripper above the drawer
        robot.move_gripper("horizontally aligned with drawer")  # move gripper to side of the drawer
        robot.move_gripper("around the drawer handle")  # move gripper around the handle
        robot.move_gripper("pull the drawer open")  # pull the drawer open by moving the gripper back