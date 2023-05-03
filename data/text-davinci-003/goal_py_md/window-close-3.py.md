

The program should read like this:

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # Start by moving the robot's gripper right of the window handle.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the gripper is already right of the window handle, push the window
    # closed.
    if check("the robot's gripper is right of the window handle"):
        robot.move_gripper("around the window handle", close_gripper=True)
    # Once the gripper has a little bit of control over the window handle, push
    # harder to close the window.
    if check("the robot's gripper is infront of the window handle and the window is not closed"):
        robot.move_gripper("left of the window handle")
```