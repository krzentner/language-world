

Followed by:

```
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.put("gripper around the handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("upward on handle")
```