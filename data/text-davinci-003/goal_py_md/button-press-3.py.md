

Then add the following code:

```
    # Steps:
    #  1. Put gripper forward aligned with button
    #  2. Press button
    # First, move the gripper to be forward aligned with the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # If the gripper is lined up in front of the button, push it.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")
```