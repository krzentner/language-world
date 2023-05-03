Here's the code to complete the `drawer-open` task:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
```

This code checks if the robot's gripper is near the drawer handle and if it is forward aligned with the handle before pulling the drawer open. If the grip is not near the handle, it grabs the handle before opening the drawer.