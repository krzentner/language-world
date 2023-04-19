Sorry, it seems like there is a duplicate `drawer_close` function in the provided code. Here's the corrected version:

# drawer-close: push the drawer close
# def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")