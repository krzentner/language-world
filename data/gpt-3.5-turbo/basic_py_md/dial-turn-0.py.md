```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the dial")
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    if check("the robot's gripper is around the dial"):
        robot.rotate("dial to the desired position")
```

Note: I had to use a bit of imagination as I don't have more information about the robot's capabilities. Please feel free to modify the instructions according to the specifications of your robot.