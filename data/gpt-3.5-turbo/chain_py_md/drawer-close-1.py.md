# drawer-close: push the drawer close
# def drawer_close(robot):
    # Steps:
    #  1. Put the gripper roughly around the drawer handle
    #  2. Push the drawer closed
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with the drawer handle"):
        robot.push("drawer closed")