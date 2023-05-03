   

Then add the code to complete the task:

```
# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not in front of button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is in front of button and the robot's gripper is not touching button"):
        robot.grab("button")
    if check("the robot's gripper is touching button"):
        robot.push("button")
```