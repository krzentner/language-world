

Next, add the code:

```
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around the handle")
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")
```