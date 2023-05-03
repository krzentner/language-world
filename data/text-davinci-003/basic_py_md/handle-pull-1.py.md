

After that, add:

```
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
```