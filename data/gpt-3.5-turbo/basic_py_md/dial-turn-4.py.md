Sure. Here's the program to perform the dial-turn task:

```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the dial is not between 40 and 60"):
        robot.grab("dial")
        robot.turn("dial to 50")
        robot.release("dial")
```

This program checks if the gripper is above the dial and if the dial is in the desired position. If the dial needs to be turned, it grabs the dial, turns it to the desired position, and releases it.