

We first want to check if the robot's gripper is in the correct position to reach the target location.

```
    if check("the robot's gripper is not in the correct position to reach the target location"):
        robot.put("gripper at correct position")
```

Then, we want to check if the robot can reach the target location without any obstructions.

```
    if check("the robot can reach the target location without any obstructions"):
        robot.reach("target location")
```

Finally, we want to check if the robot is in the correct position relative to the target location.

```
    if check("the robot is not in the correct position relative to the target location"):
        robot.align("gripper to target location")
```