

The program should check that the robot's gripper is not above the dial, then move the gripper near the dial, and turn the dial clockwise.

```
# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not above the dial"):
        robot.move("gripper near dial")
    if check("the robot's gripper is near the dial"):
        robot.turn("dial clockwise")
```