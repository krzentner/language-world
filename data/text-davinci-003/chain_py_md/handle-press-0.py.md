

Steps:
1. Put gripper above the handle
2. Line up the gripper vertically with the handle
3. Push the handle downwards

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Line up the gripper vertically with the handle
    #  3. Push the handle downwards
    # If the gripper is not above the handle yet, put the gripper above it.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above the handle")
    # If the gripper is above the handle and not vertically aligned, move the
    # gripper vertically.
    if check("the robot's gripper is above the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.align("gripper with handle")
    # After the gripper is vertically aligned with the handle, push down on it.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("handle downwards")
```