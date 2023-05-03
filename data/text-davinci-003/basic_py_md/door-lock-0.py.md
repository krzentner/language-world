

Then, add the implementation:

```
# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not above the door dial"):
        robot.put("gripper above door dial")
    if check("the robot's gripper is above the door dial and the robot's gripper is not near the dial"):
        robot.grab("dial")
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.close("gripper around the dial")
    if check("the robot's gripper is closed and the dial is not in the locked position"):
        robot.turn("dial to the locked position")
```