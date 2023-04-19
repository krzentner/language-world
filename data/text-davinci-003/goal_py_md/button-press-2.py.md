

Then, fill in the function text:

```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # To line up the gripper from the front, we just need to line up the 
    # gripper from side to side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("forward aligned with the button")
```