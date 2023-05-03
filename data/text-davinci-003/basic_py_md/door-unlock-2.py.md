

Then add the code for the program:

```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not nearly above the dial"):
        robot.put("gripper nearly above dial")
    if check("the robot's gripper is nearly above the dial and the robot's gripper is open"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise")
    if check("the dial is in the correct position"):
        robot.stop("turning dial")
```