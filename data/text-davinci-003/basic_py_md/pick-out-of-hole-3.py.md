

Then, add the following code:

```
    if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.grab("peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.place("peg at goal")
```