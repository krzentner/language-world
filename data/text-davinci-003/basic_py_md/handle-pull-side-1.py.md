

The code to complete the program is as follows:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is around handle and the handle is not pulled up"):
        robot.pull("handle up")
```