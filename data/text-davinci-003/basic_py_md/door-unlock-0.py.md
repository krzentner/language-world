

Then add code to the function.

```
# door-unlock: turn the dial on the door
def door_unlock(robot):
    if check("the robot's gripper is not nearly vertically aligned with the door dial"):
        robot.put("gripper above door dial")
    if check("the robot's gripper is almost vertically aligned with the door dial and the robot's gripper is not around door dial"):
        robot.put("gripper around door dial")
    if check("the robot's gripper is around door dial and the door dial is not facing up"):
        robot.turn("door dial up")
    if check("the door dial is facing up and the door dial is not next to the wall"):
        robot.turn("door dial left")
    if check("the door dial is next to the wall and the door dial is not aligned with the wall"):
        robot.turn("door dial right")
    if check("the door dial is aligned with the wall"):
        robot.unlock("door")
```