

Continue with the following code:

```
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, put the gripper above the button.
    # Because this is a "topdown" action, we just need to line up the gripper
    # from above.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")
```