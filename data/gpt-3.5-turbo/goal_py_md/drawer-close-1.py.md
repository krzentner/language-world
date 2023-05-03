```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above the center of the drawer
    #  2. Push the drawer closed
    # To close the drawer, we need to put the gripper above the center of the drawer.
    if check("the robot's gripper is not above the center of the drawer"):
        robot.move_gripper("above the center of the drawer")
    # Once the gripper is above the center of the drawer, we can push it closed.
    if check("the robot's gripper is above the center of the drawer"):
        robot.move_gripper("right of the drawer handle")