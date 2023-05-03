

The steps for this task are as follows:

1. Put gripper above button 
2. Lower gripper onto top of button
3. Push button downward 

The code for this task would be: 

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button 
    #  2. Lower gripper onto top of button
    #  3. Push button downward 

    # If the gripper is not above the button, move it to be above the button.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # If the gripper isn't on top of the button yet, lower it to be on it.
    if check("the robot's gripper is above button and the robot's gripper is not on top of the button"):
        robot.move_gripper("on top of the button", close_gripper=True)
    # If the gripper is on top of the button and is already closed, push it down.
    if check("the robot's gripper is on top of the button and the robot's gripper is closed"):
        robot.move_gripper("below the button")
```