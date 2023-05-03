

Here is the code to complete the hammer task:

```
# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    if check("the robot's gripper is vertically aligned with the hammer and the robot's gripper is not around hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is around the hammer and the robot's gripper is not near the nail"):
        robot.move("gripper near nail")
    if check("the robot's gripper is near the nail and the hammer is above the nail"):
        robot.hit("nail with hammer")
```