Here's the program to complete the last task, `drawer-close`:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("towards drawer")
    if check("the robot's gripper is in front of drawer handle and drawer is closed"):
        robot.release("gripper from handle")
```

This program first checks if the gripper is above the drawer handle and around the drawer handle. It then pushes the drawer towards the closed position. Finally, it releases the gripper from the handle once the drawer is closed.