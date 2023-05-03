

The robot should use the hammer to hit the nail. The code should be structured like this:

```
# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.put("gripper above nail")
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is open"):
        robot.put("gripper around hammer handle")
    if check("the robot's gripper is around hammer handle"):
        robot.move("hammer down towards nail")
    if check("the hammer is close to the nail"):
        robot.hit("hammer on nail")
```