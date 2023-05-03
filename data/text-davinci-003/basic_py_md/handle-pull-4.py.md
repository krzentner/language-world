

Then add the code that will execute this task:

```
# handle-pull: pull up the handle
def handle_pull(robot):
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up") 
```