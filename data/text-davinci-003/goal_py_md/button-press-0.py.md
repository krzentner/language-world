
The full program should have the following steps:

1. Put gripper front of the button 
2. Close gripper around button 
3. Push down on button

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper front of the button
    #  2. Close gripper around button
    #  3. Push down on button
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Then, close the gripper around the button.
    if check("the robot's gripper is forward aligned with button and the robot's gripper is not closed around button"):
        robot.move_gripper("around the button", close_gripper=True)
    # Finally, push down on the button.
    if check("the robot's gripper is closed around button"):
        robot.move_gripper("below the button")
```