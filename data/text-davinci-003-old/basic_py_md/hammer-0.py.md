

Here's the code to perform the task:

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    if check("the robot's gripper is not near the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is near the hammer and the hammer is not above the nail"):
        robot.put("hammer above nail")
    if check("the hammer is above the nail"):
        robot.hit("hammer on nail")
```