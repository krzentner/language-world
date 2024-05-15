

Then, complete the code:

```
# window-open: slide the window open to the left
def window_open(robot):
    if check("the window handle is to the left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")
```