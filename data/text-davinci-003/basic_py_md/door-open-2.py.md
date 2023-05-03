

Then add:

```
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around the door handle"):
        robot.pull("away from door")
```