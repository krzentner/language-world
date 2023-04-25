

Your code should be:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle and the handle is below the robot's gripper"):
        robot.pull("handle up")
```