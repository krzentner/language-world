

Solution: 

```
# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the robot's gripper is not right of the window handle, move it there.
    if check("the robot's gripper is not right of the window handle"):
        robot.put("gripper right of the window handle")
    # If the robot's gripper is near the window handle, we can attempt to slide
    # the window open by pushing it from the side.
    if check("the robot's gripper is near the window handle"):
        robot.push("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # we need to push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")
```