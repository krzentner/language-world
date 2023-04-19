

Here is the program to perform the task `handle-pull`:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")
```