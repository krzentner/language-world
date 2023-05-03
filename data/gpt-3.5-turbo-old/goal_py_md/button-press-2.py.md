```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Move gripper above button
    #  2. Move gripper forward so it's between the button and the wall
    #  3. Push the button
    # First, move the gripper vertically above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Next, move the gripper horizontally forward so it's between the button
    # and the wall.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Finally, push the button.
    if check("the robot's gripper is in front of the button"):
        robot.move_gripper("against the button")
```