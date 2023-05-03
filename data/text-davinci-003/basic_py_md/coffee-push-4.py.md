

Then add the code:

```
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near the mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above the mug and the robot's gripper is closed"):
        robot.slide("mug to goal")
```