

The program should have the robot move a cube from its current location to a target location.

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not near the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move("gripper to goal with cube")
    if check("the robot's gripper is near the target"):
        robot.put("cube down at goal")
```