Sorry, it looks like the drawer-close function is repeated. Here's a new function:

# drawer-close: push the drawer close
# def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is backward aligned with drawer handle"):
        robot.push("drawer closed")