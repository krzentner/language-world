

We'll need to put the gripper near the handle, since it's just pushing down.

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # Put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near the handle")
    # Once the gripper is near the handle, push down on it.
    if check("the robot's gripper is near the handle"):
        robot.push("down on the handle")
```