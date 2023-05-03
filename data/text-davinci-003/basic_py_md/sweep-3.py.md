

The code is as follows:

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is around cube and the robot's gripper is closed"):
        robot.sweep("cube to goal")
```