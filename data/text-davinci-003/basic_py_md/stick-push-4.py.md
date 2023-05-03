

Then, fill in the program:

```
# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the stick is not left of the robot's gripper and the stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with the stick and the robot's gripper is not near the thermos"):
        robot.align("stick to thermos")
    if check("the robot's gripper is near the thermos and the robot's gripper is not around the stick"):
        robot.put("gripper around stick")
    if check("the robot's gripper is around the stick and the thermos is below the robot's gripper"):
        robot.slide("thermos to goal")
```