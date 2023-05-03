

Then your code:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")
```