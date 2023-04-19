

Here is the program:

```
# button-press-topdown: push the button down from above
# def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Once the gripper is lined up above the button, line it up exactly.
    if check("the robot's gripper is above the button and the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")
```