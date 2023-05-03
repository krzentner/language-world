

Then, complete the function:

```
# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Push the window open
    #  3. Keep pushing the window open
    # First, put the gripper right of the window handle, so that the robot will
    # be pushing the window open when it moves the gripper back.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle, we can start pushing the
    # window open.
    if check("the robot's gripper is near the window handle"):
        robot.push("window left")
    # If the robot's gripper is already in front of the window handle, then we
    # need to push harder to open the window further.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")
```