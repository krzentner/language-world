

Then fill in the appropriate code:

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is near to the target bin"):
        robot.put("cube in bin")
```