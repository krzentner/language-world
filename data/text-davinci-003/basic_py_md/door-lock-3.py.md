

Then, you can add the rest of the code to perform the task:

```
# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the door knob"):
        robot.grab("door knob")
    if check("the robot's gripper is near the door knob and the door knob is not aligned with goal"):
        robot.turn("door knob to goal")
    if check("the door knob is aligned with goal"):
        robot.lock("door knob")
```