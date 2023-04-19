

Solution:

```
# door-unlock: turn the dial on the door
# def door_unlock(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.move("gripper to near the door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around the door handle")
    if check("the robot's gripper is around the door handle"):
        robot.turn("dial to unlock the door")
```