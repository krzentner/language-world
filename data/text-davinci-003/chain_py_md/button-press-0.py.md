

Then add the following code:

```
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button
    # Because we want to press the button from the front, line up the gripper
    # in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.align("gripper to button")
    # Now that the gripper is lined up, push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")
```