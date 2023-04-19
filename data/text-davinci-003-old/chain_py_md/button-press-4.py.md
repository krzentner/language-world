

The program should look like this:

```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the front
    # To press the button from the front, we need to line up the gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")
```