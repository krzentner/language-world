```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Push drawer closed
    # First, put the gripper mostly above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # If the gripper is lined up with the handle, we can start pushing the drawer
    # closed.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("right of the drawer handle")