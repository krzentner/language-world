Here's the program to perform the `button-press-topdown` task:

```
# button-press-topdown: push the button down from above
# def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")
```

This program first checks if the robot's gripper is not vertically aligned with the button. If so, it moves the gripper to be in line with the button and closes the gripper around it. Once this is done, it checks if the gripper is vertically aligned with the button, and if so, it moves the gripper closer to the button to push down on it.