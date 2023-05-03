```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.grab("dial")
    if check("the robot's gripper is above the dial and the dial is not aligned with goal"):
        robot.align("dial to goal")
    if check("the dial is aligned with goal"):
        robot.twist("dial to the correct position")
```