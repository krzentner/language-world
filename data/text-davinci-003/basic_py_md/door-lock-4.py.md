

Then fill in the code:

```
# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not almost vertically aligned with the door dial"):
        robot.put("gripper above door dial")
    if check("the robot's gripper is almost vertically aligned with the door dial and the robot's gripper is open"):
        robot.put("gripper around door dial")
    if check("the robot's gripper is around the door dial"):
        robot.turn("door dial clockwise")
```