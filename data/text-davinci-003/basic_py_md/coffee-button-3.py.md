

Solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    if check("the robot's gripper is not near the coffee button"):
        robot.put("gripper above coffee button")
    if check("the robot's gripper is near the coffee button but not vertically aligned with it"):
        robot.align("gripper vertically with coffee button")
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("on coffee button")
```