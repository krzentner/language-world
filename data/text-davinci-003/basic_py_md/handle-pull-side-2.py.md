 

and then fill in the following code.

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not forward aligned with handle"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("handle up")