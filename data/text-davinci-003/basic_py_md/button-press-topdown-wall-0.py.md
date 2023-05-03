

Next, we will test the conditions first:

```
    if check("the robot's gripper is not vertically aligned with button and the wall is in the way"):
        robot.move("gripper around wall to above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```
Finally, we end the function:

```
    return
```