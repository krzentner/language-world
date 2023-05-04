Here is the code to perform the `button-press-topdown` task:

```
# button-press-topdown: push the button down from above
# def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```

In the first step, we check if the gripper is already lined up above the button. If it is not, we move it to be above the button.

In the second step, we assume that the gripper is already lined up above the button, so we directly push down on the button.