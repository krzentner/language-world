

Then, fill in the code:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not above the door lock"):
        robot.put("gripper above door lock")
    if check("the robot's gripper is not around the door lock and the robot's gripper is open"):
        robot.drop("gripper around door lock")
    if check("the robot's gripper is around the door lock and the robot's gripper is open"):
        robot.close("gripper around door lock")
    if check("the robot's gripper is around the door lock and the robot's gripper is closed"):
        robot.turn("dial clockwise")
```