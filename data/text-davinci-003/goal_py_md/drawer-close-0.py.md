

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper right of the drawer handle
    #  2. Start pushing against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # To start closing the drawer, we should put the gripper to the right of the
    # drawer handle.
    if check("the robot's gripper is not right of the drawer handle"):
        robot.move_gripper("right of the drawer handle")
    # If the gripper is getting close to the drawer handle, we can start pushing
    # on it.
    if check("the robot's gripper is in front of the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # if the gripper is aligned with the drawer handle, we can push the drawer
    # closed fully.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")