

Solution:

```
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    if check("the robot's gripper is not near the mug"):
        robot.move("gripper to mug")
    if check("the robot's gripper is near the mug and the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is not around mug"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is around mug and not near the goal"):
        robot.move("mug to goal")
    if check("the robot's gripper is near the goal"):
        robot.place("mug at goal")
```