

Solution:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper left/right of the handle
    #  2. Push down on the handle
    # To press the handle down from the side, we need to move the gripper to the
    # side of the handle.
    if check("the robot's gripper is not left/right of the handle"):
        robot.move_gripper("left/right of the handle")
    # Once the gripper is lined up with the handle from the side, just push
    # down.
    if check("the robot's gripper is left/right of the handle"):
        robot.move_gripper("near the handle")
```