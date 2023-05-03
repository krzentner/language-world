Here's the code for `window_close`:

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # First, put the gripper to the left of the window handle to be able to push
    # against it.
    if check("the robot's gripper is not left of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the gripper is already left of the window handle, we can start pushing
    # to close the window.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
``` 

This function moves the gripper to the left of the window handle and then pushes against the handle to close the window.