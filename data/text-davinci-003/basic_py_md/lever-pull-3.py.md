

The program should rotate the lever up.

```
# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not near the lever and the robot's gripper is not above the lever"):
        robot.reach("the lever")
    if check("the robot's gripper is near the lever and the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is above the lever"):
        robot.rotate("lever up")
```