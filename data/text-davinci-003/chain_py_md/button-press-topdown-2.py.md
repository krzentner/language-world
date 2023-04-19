

The rest of the program should be:

```
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, line up the robot's gripper as viewed from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```