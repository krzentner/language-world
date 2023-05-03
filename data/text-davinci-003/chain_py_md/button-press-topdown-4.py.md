

Then write the code

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push button down
    # Grab the button by putting the gripper above it
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # We should now be almost lined up, close the gripper on the button
    if check("the robot's gripper is almost vertically aligned with the button and gripper is open"):
        robot.close("gripper around button")
    # Finally, push the button down
    if check("the button is below the robot's gripper and the robot's gripper is closed"):
        robot.push("button down")
```