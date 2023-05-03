# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move("gripper to the drawer handle")
    if check("the robot's gripper is near the drawer handle and the robot's gripper is not around the handle"):
        robot.grab("the drawer handle")
    if check("the robot's gripper is around the drawer handle"):
        robot.push("the drawer closed")