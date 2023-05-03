

Solution

```
# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on the button
    # We need to put the gripper above the button before we can push it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # Once the gripper is lined up above the button, push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button", close_gripper=True)
    # Now that the gripper is nearer the button, we can push the button by
    # pushing the gripper downwards.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("below the button")
```