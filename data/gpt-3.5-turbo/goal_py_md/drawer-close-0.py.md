# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Push the drawer closed
    # First, put the gripper to the left of the drawer handle.
    if check("the robot's gripper is not left of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # Once the gripper is to the left of the handle, push the drawer closed by
    # moving the gripper to the right of the handle.
    if check("the robot's gripper is left of the drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")