

The rest of the program:

```
# Steps:
#  1. Put gripper above button on the coffee machine
#  2. Push down on the button from the top

# First, the gripper needs to line up the button as seen from above.
if check("the robot's gripper is not vertically aligned with the button"):
    robot.put("gripper above the button")
# Once lined up, the gripper should be able to press the button by pushing down on it.
if check("the robot's gripper is vertically aligned with the button"):
    robot.push("down on the button")
```