

Solution:
```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not near the mug"):
        robot.put("gripper near the mug")
    if check("the robot's gripper is not aligned with the mug"):
        robot.align("gripper to the mug")
    if check("the robot's gripper is aligned with the mug and the robot's gripper is open"):
        robot.drop("gripper around the mug")
    if check("the robot's gripper is around the mug and the robot's gripper is closed"):
        robot.slide("mug to the goal")
```