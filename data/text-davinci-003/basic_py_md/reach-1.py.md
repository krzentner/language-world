

The robot should move its gripper to the target location and hold it there, ready for further action.

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not above the target location"):
        robot.put("gripper above the target location")
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location"):
        robot.hold("gripper in place")
```