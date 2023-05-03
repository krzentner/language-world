

The program would then look like this:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper horizontally with handle")
    if check("the robot's gripper is horizontally aligned with the handle and the handle is not facing up"):
        robot.pull("handle up")
```