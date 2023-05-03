

Next, add the code to perform the task:

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick")
    if check("the robot's gripper is above thermos and the robot's gripper is closed"):
        robot.drag("thermos to goal")
```