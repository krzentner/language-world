

Steps: 
1. Put gripper above the button
2. Drop gripper around the button
3. Push the button

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper around the button
    #  3. Push the button
    # First, put the gripper above the button, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper isn't around the button, put it around the button.
    if check("the robot's gripper is not around button and the robot's gripper is open"):
        robot.drop("gripper around button")
    # If the gripper is near the button and open, maybe we can push it by closing
    # the gripper.
    if check("the robot's gripper is near button and the robot's gripper is open"):
        robot.close("gripper around button")
    # We closed the gripper, and the button is still near the gripper, so maybe we
    # grabbed it.
    # Try to push the button.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above button and the robot's gripper is closed"):
        robot.push("down on button")
```