

Here's the solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the coffee button
    #  2. Lower the gripper onto the button
    #  3. Press the button
    # First, make sure the gripper is lined up above the button.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.put("gripper above coffee button")
    # Once the gripper is aligned with the button, lower it onto the button.
    if check("the robot's gripper is vertically aligned with coffee button and the robot's gripper is not over button"):
        robot.drop("gripper onto button")
    # If the gripper is now over the button, press the button with the gripper.
    if check("the robot's gripper is over button"):
        robot.press("button")
```