

and end with:

```
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
```

The program should demonstrate how the robot can reach a target location. 

```
# reach: reach to the target location
# def reach(robot):
    if check("the robot's gripper is not near the target"):
        robot.move("gripper to target")
    if check("the robot's gripper is not close enough to the target"):
        robot.adjust("gripper closer to target")
    if check("the robot's gripper is close enough to the target"):
        robot.reach("to goal")
```