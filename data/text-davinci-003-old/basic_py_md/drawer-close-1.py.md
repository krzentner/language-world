

Here is the program to perform the task `drawer-close`:

```
# drawer-close: push the drawer close
# def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")
``