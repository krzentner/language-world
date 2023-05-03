

Answer: 
```
# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push in the button
    # Because this is a button press, we need to line up the gripper from the
    # front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, just push in the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("in on button")