

Solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    if check("the robot's gripper is not near the coffee machine button"):
        robot.put("gripper above coffee machine button")
    if check("the robot's gripper is not above the coffee machine button"):
        robot.put("gripper above coffee machine button")
    if check("the robot's gripper is above the coffee machine button"):
        robot.push("down on coffee machine button")
```