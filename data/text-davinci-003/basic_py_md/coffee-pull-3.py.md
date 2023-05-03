

The code for this task should look something like this:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    if check("the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    if check("the robot's gripper is not near the mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    if check("the robot's gripper is near the mug handle"):
        robot.pull("mug to goal")
```