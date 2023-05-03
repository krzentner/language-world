

Then add your code:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above the button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.push("gripper into the button")
    if check("the robot's gripper is near the button and the button is not below the robot's gripper"):
        robot.slide("the button downward")
    if check("the button is below the robot's gripper"):
        robot.push("button downward until it clicks")
```