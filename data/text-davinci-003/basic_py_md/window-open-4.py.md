

Then add the code:

```
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("the gripper to the right of the window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")
```