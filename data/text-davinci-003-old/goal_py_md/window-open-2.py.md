

The program should go as follows:

```
# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not right of the window handle, move it there.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # Once the robot's gripper is near the window handle, start pushing the window open.
    if check("the robot's gripper is not in front of the window handle"):
        robot.move_gripper("in front of the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder to open the window all the way.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
```