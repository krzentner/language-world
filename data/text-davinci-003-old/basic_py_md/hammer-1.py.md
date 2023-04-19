

Solution:

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    if check("the robot's gripper is not above the nail"):
        robot.place("gripper above nail")
    if check("the robot's gripper is not around the hammer"):
        robot.drop("gripper around hammer")
    if check("the robot's gripper is around the hammer and the robot's gripper is not near the nail"):
        robot.move("gripper near nail")
    if check("the robot's gripper is near the nail and the robot's gripper is around the hammer"):
        robot.hit("hammer on nail")
```