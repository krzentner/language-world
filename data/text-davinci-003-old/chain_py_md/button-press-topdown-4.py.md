

The program should be:

```
# button-press-topdown: push the button down from above
# def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```