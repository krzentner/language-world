

In this example, the robot needs to grab a coffee mug and move it to a target location.

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the coffee mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is near mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around mug"):
        robot.move("mug to goal")
```