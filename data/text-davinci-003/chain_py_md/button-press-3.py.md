

Here is the code:
```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper in front of the button
    #  2. Push down on the button
    # We have to line the robot's gripper up in front of the button before we
    # can push on it.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # Once the gripper is lined up, we can push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")
```