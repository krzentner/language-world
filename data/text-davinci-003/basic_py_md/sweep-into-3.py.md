

Then add the code:

```
    if check("the robot's gripper is not near the cube"):
        robot.reach("to the cube")
    if check("the robot's gripper is not above the cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near the cube and the cube is not above the robot's gripper"):
        robot.raise("gripper with cube")
    if check("the robot's gripper is above the cube"):
        robot.slide("cube to goal")
```