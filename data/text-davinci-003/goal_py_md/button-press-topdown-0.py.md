

Then complete the program:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the button is below the robot's gripper, push the button down.
    if check("the button is below the robot's gripper"):
        robot.move_gripper("above the button")