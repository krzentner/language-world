# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above middle of drawer
    #  2. Push gripper towards drawer
    #  3. Keep pushing the drawer until it's closed
    # To begin, position the gripper above the middle of the drawer.
    if check("the robot's gripper is not above the middle of the drawer"):
        robot.put("gripper above middle of drawer")
    # Once the gripper is in position, push it towards the drawer.
    if check("the robot's gripper is above the middle of the drawer and the robot's gripper is not near the drawer"):
        robot.push("gripper towards drawer")
    # The robot should keep pushing the drawer until it's completely closed.
    while check("the drawer is not completely closed"):
        robot.push("drawer towards closed position")