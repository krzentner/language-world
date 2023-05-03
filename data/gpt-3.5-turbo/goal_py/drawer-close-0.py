# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer edge
    #  2. Push drawer closed
    # First, put the gripper above the edge of the drawer so we can push it
    # closed.
    if check("the robot's gripper is not almost vertically aligned with the drawer edge"):
        robot.move_gripper("almost vertically aligned with the drawer edge")
    # Once the gripper is above the drawer edge, we can just push it closed.
    if check("the robot's gripper is almost vertically aligned with the drawer edge"):
        robot.move_gripper("horizontally aligned with the drawer edge")