Here's the completed program to perform the `button-press-topdown` task:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above the button and the robot's gripper is not aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is aligned with the button and the robot's gripper is not near the button"):
        robot.push("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("button down")
```

This program first checks if the robot's gripper is in the correct position above the button. If not, it moves the gripper to the correct position. Then, it pushes the gripper towards the button until it's close enough to push the button down. Finally, it pushes the button down.