

Steps:
1. Put gripper above the handle.
2. Drop gripper around the handle.
3. Push down the handle.

Solution:
```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Push down the handle
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and gripper is not around handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")
```