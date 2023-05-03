

Solution:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    if check("the robot's gripper is not above the doorknob"):
        robot.put("gripper above the doorknob")
    if check("the robot's gripper is not horizontally aligned with the doorknob"):
        robot.align("gripper horizontally with the doorknob")
    if check("the robot's gripper is horizontally aligned with the doorknob"):
        robot.turn("dial clockwise or counterclockwise to lock or unlock the door")
```