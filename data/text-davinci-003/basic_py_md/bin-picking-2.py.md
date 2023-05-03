

Then add the following code:

```
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.grab("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is carrying cube and the target bin is not near"):
        robot.move("gripper to bin")
    if check("the robot's gripper is carrying cube and the target bin is near"):
        robot.place("cube in bin")
```