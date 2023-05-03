Sure, here's the code you need:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer"):
        robot.reach("to the drawer")
    if check("the robot's gripper is not above the drawer handle"):
        robot.move("gripper above drawer handle")
    if check("the robot's gripper is above drawer handle and the robot's gripper is not around drawer handle"):
        robot.drop("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("drawer closed")
```

Let me know if you need further assistance.