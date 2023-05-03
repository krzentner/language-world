

Then complete the program:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not near handle"):
        robot.reach("to handle")
    if check("the robot's gripper is forward aligned with handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")