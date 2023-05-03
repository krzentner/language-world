# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # First, put the gripper roughly around the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer handle is to the right of the gripper, move the gripper
    # slightly to the left of the handle so we can pull it open.
    if check("the drawer handle is not left of the robot's gripper"):
        robot.move_gripper("left of the drawer handle")
    # Once the gripper is to the left of the handle, we can pull the drawer open.
    if check("the robot's gripper is left of the drawer handle"):
        robot.move_gripper("pull open the drawer")