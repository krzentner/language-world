

Solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above the button"):
        robot.push("button")
```