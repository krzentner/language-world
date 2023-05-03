

Steps:
1. Put gripper to the left of window handle 
2. Push window closed harder
3. Check that the window is fully closed

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Push the window closed harder
    #  3. Check that the window is fully closed
    # First, put the gripper roughly left of window handle, so that we don't bump it while
    # trying to close it.
    if check("the robot's gripper is not left of the window handle"):
        robot.place("gripper left of window handle")
    # If the gripper is near the window handle, start pushing it closed.
    if check("the robot's gripper is near window handle and the window is not completely closed"):
        robot.push("window closed harder")
    # If the window is not completely closed, push harder. 
    if check("the window is not completely closed"):
        robot.push("window closed harder")
    # If the window is fully closed, check that it is and stop pushing.
    if check("the window is fully closed"):
        robot.stop("pushing window closed")
```