

This task requires the robot to push a button on a coffee machine.

Steps: 
1. Put the gripper above the button. 
2. Level the gripper with the button. 
3. Push the button.

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Line up gripper with button
    #  3. Push the button
    # First, put the gripper above the button, so that we don't bump it while
    # trying to press it.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper isn't lined up with the button, move it to the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.level("the gripper with the button")
    # Once the gripper is lined up with the button, we can just press the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button")
````