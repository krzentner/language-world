

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of window handle
    #  2. Push window right
    #  3. Put gripper back near window handle
    if check("the robot's gripper is below the window handle"):
        robot.place("gripper near window handle")
    if check("the robot's gripper is below the window handle and the robot's gripper is near window handle"):
        robot.push("window right")
```

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of window handle
    #  2. Push window right
    #  3. Put gripper back near window handle
    if check("the robot's gripper is below the window handle"):
        robot.place("gripper near window handle")
    if check("the robot's gripper is below the window handle and the robot's gripper is near window handle"):
        robot.push("window right")
    if check("the robot's gripper is right of the window handle"):
        robot.place("gripper near window handle")
```

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of window handle
    #  2. Push window right
    #  3. Put gripper back near window handle
    if check("the robot's gripper is below the window handle"):
        robot.place("gripper near window handle")
    if check("the robot's gripper is below the window handle and the robot's gripper is near window handle"):
        robot.push("window right")
    if check("the robot's gripper is right of the window handle"):
        robot.place("gripper near window handle")
    if check("the robot's gripper is near window handle"):
        robot.push("window right")
```

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of window handle
    #  2. Push window right