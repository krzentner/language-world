

Solution:

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is around the mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is around the mug and the robot's gripper is closed"):
        robot.pull("mug to goal")
```