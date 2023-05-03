

Your code should look like this:

```
# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
    if check("the robot's gripper is near the handle"):
        robot.release("handle")
```