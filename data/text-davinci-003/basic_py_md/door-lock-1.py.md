

Then use the following instructions to complete the program:

1. If the robot's gripper is not close to the door handle, move the robot to grab the handle.
2. If the robot's gripper is near the door handle and the door handle is not rotated, rotate the handle downwards.
3. If the robot's gripper is near the door handle and the handle is rotated down, rotate the handle clockwise until the door is locked.
4. Let go of the handle.

```
# door-lock: turn the dial on the door
def door_lock(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle and the door handle is not rotated"):
        robot.rotate("door handle downwards")
    if check("the robot's gripper is near the door handle and the handle is rotated down"):
        robot.rotate("clockwise until door is locked")
    if check("the robot's gripper is near the door handle"):
        robot.release("door handle")
```