

The goal of this task is to push the button on the coffee machine.

Steps:

1. Put the gripper above the button
2. Push the button

First, put the gripper above the button so that it can be vertically aligned with it.

```
if check("the robot's gripper is not above button"):
    robot.put("gripper above button")
``` 

Once the gripper is above the button, push the button down.

```
if check("the robot's gripper is above button"):
    robot.push("down on button")
```