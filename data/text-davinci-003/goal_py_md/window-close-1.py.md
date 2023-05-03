
    
Then add code:

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not near the window handle, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the gripper is aligned with the window handle but not touching it,
    # move the gripper to the right to push the window closed.
    if check("the robot's gripper is vertically aligned with the window handle and the robot's gripper is not touching the window handle"):
        robot.move_gripper("right of the window handle")
```