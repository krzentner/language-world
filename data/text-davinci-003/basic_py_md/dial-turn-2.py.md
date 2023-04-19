

The following code:

```
# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.put("gripper near dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the dial is in the right notched position"):
        robot.turn("dial right")
    if check("the robot's gripper is around the dial and the dial is in the left notched position"):
        robot.turn("dial left")
```