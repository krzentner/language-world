

Here's the code for `button_press_topdown`:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down on the button
    #  3. Press the button further down
    # The robot should put the gripper above the button, before dropping the 
    # gripper onto the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Once the gripper is above the button, pushing down on the button should
    # trap it.
    if check("the robot's gripper is above the button and the button is not below the robot's gripper"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is trapping the button and the button is not pressed down
    # enough, press down on the button harder.
    if check("the robot's gripper is trapping the button and the button is not pressed down"):
        robot.move_gripper("further down the button")
```