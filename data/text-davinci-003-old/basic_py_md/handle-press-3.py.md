

Solution:

```
# handle-press: push down the handle
# def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("the gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on the handle")
```