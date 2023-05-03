# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move("gripper to drawer handle")
    if check("the robot's gripper is near the drawer handle and the drawer is open"):
        robot.push("drawer closed")