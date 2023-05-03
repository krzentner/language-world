

The code would look like this:
```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is aligned with the cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around cube and the cube is not near the goal"):
        robot.sweep("cube to goal")
    if check("the cube is at goal and the robot's gripper is closed"):
        robot.open("gripper and release cube")
```