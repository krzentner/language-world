

Then, add the commands:

```
    if check("the robot's gripper is not above the box"):
        robot.place("gripper above box")
    if check("the robot's gripper is not around box and the robot's gripper is open"):
        robot.grab("gripper around box")
    if check("the robot's gripper is near box and the robot's gripper is open"):
        robot.close("gripper around box")
    if check("the robot's gripper is above box and the robot's gripper is closed"):
        robot.place("box at goal")
```