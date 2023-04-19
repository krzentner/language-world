

Solution:

```
# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around the edge of the dial"):
        robot.drop("gripper around dial edge")
    if check("the robot's gripper is around the edge of the dial"):
        robot.turn("dial clockwise/counterclockwise")
```