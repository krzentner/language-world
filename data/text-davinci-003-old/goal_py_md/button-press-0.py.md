

Then add the steps to complete the task, using the `check` function to determine the robot's state:

```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # Because this is "front", we just need to line up the gripper from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")
```