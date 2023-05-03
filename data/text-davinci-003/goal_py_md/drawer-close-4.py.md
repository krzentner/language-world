

From the code, we know that the robot's gripper should be around the drawer handle to pull the drawer open. To close the drawer, we can use the reverse steps.

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper around the drawer handle
    #  2. Push to close the drawer
    # First, grip the drawer handle.
    if check("the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # If the gripper is around the drawer handle, we can push to close it.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")