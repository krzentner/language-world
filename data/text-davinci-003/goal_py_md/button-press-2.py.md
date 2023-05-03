

Then add the following code:

```
    # Steps:
    #  1. Line up the gripper to the button
    #  2. Push down on the button
    # Line the gripper up with the button from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")
```