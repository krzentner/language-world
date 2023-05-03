

Then, add the following code to the program:

```
    # Steps:
    #  1. Align the gripper with the button from the front
    #  2. Push down on the button
    # To start, line the robot's gripper up with the button from the front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.align("gripper with the button")
    # Once the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("down on button")
```