

Solution:
```
# hammer: hit the nail with the hammer
# def hammer(robot):
    if check("the robot's gripper is not close to the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is close to the hammer and the robot's gripper is not near the nail"):
        robot.position("gripper near nail")
    if check("the robot's gripper is near the nail"):
        robot.swing("hammer at nail")