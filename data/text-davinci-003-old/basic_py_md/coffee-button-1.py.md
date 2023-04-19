

Solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.close("gripper around button")
    if check("the robot's gripper is above the button and the robot's gripper is closed"):
        robot.push("down on button")
```