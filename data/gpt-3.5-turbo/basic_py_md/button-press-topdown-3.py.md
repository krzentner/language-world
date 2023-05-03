```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above the button"):
        robot.move("gripper above button")
    if check("the robot's gripper is vertically aligned with the button" and "the robot's gripper is not near the button"):
        robot.move("gripper near button")
    if check("the robot's gripper is near the button"):
        robot.push("button down")
```