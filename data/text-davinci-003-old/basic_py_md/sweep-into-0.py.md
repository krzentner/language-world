

The program should be as follows:

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not near the cube"):
        robot.reach("to cube")
    if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around the cube"):
        robot.sweep("cube to goal")
```