

Then add your code:

```
# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.grab("gripper to the side of the button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("the button")
```