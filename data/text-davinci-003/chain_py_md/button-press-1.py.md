

Steps:
1. Place the gripper directly in front of the button.
2. Push the button with the gripper.

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Push the button with the gripper
    # First, move the gripper in front of the button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.place("gripper in front of button")
    # Once the gripper is lined up, push the button with the gripper.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.push("button")
```