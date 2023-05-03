

Here's the solution:

```
# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button
    #  3. Push the button
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the button isn't below the gripper as seen from above, move the gripper
    # above the button.
    if check("the robot's gripper is not directly above the button and the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to push it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.move_gripper("just above the button", close_gripper=True)
    # If the gripper is near the button, close the gripper and push the button.
    if check("the robot's gripper is near the button and the button is below the robot's gripper"):
        robot.move_gripper("just above the button")