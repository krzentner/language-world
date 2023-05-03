# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above the drawer from the side
    #  2. Start pushing against the drawer to close it
    #  3. Push the drawer closed harder
    # We need to put the gripper above the drawer from the side since the drawer
    # will be pushed closed.
    if check("the robot's gripper is not vertically aligned with the drawer and the robot's gripper is not to the side of the drawer"):
        robot.move("gripper to side of drawer and above it")
    # If the robot's gripper is in the right position, we can start pushing the
    # drawer closed.
    if check("the robot's gripper is to the side of the drawer and the robot's gripper is near the drawer"):
        robot.push("drawer closed")
    # If the robot's gripper is starting to be at the end of the drawer, push
    # harder to make sure it closes all the way.
    if check("the robot's gripper is at the end of the drawer"):
        robot.push("drawer closed harder")