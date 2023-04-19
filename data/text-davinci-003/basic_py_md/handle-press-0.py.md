

The code for handle press would then look like this:

```
# handle-press: push down the handle
# def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around the handle"):
        robot.grab("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")
```