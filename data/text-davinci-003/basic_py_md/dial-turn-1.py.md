

Your code should be something like this:

```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.drop("gripper around the dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise/counterclockwise")
```