

The program should look like this:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Push against the handle to press it down
    # Put the gripper to the side of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # Now that the gripper is near the handle, we should be able to push against
    # it to press it down.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("near the handle")
```