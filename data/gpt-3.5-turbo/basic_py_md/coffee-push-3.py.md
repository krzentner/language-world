Here is a program to perform the `coffee-push` task:

```
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is above mug and the mug is not obstructed"):
        robot.lift("mug")
    if check("the robot's gripper is above the target location"):
        robot.put("mug at target location")
    if check("the task is complete"):
        robot.complete("task")
```

Note that the `coffee-push` task involves grabbing a mug and moving it to a target location. The program uses the gripper to pick up the mug and move it to the target location. It also includes checks to make sure that the gripper is in the correct position before performing each action, and a final check to mark the task as complete.