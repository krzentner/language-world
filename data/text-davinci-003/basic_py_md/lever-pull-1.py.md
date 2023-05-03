

The program should be: 

```
# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not nearly vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is nearly vertically aligned with the lever and the robot's gripper is not around lever"):
        robot.drop("gripper around lever")
    if check("the robot's gripper is around lever and the lever is not up"):
        robot.pull("lever up")
```