

Steps:
1. Put gripper left of the handle
2. Push down the handle from the side

If the robot's gripper is not near the handle, move it near the handle. We don't need to be careful about direction, since the handle is larger than the gripper.
```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Push down the handle from the side
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the handle is left of the robot's gripper, just push down the handle.
    if check("the handle is left of the robot's gripper"):
        robot.move_gripper("left of the handle")