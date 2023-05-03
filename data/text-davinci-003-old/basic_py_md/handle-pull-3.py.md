

Your code should look like this:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
```