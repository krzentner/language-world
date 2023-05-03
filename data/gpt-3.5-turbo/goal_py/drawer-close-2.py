# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper next to the drawer handle
    #  2. Push the drawer closed
    # To close the drawer, we need to move the gripper next to the drawer handle.
    if check("the robot's gripper is not next to the drawer handle"):
        robot.move_gripper("next to the drawer handle")
    # Once the gripper is next to the drawer handle, we can push the drawer closed
    # by moving the gripper horizontally away from the drawer handle.
    if check("the robot's gripper is next to the drawer handle"):
        robot.move_gripper("horizontally away from the drawer handle")