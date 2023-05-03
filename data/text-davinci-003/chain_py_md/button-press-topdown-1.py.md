

The steps for this task are: 
1. Put the gripper above the button 
2. Drop the gripper on thebutton 
3. Press the button down

Here's the full program:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper on button
    #  3. Press button down
    # First, put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the button is aligned with the gripper, we can drop the gripper on the
    # button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is open"):
        robot.drop("gripper on button")
    # If the gripper is on the button, press the button down.
    if check("the robot's gripper is around the button"):
        robot.push("button down")
```