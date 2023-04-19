

Steps:
1. Put gripper horizontally aligned with the button
2. Push down on the button 

```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Put gripper horizontally aligned with the button
    #  2. Push down on the button
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")
```