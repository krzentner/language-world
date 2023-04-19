

Then, add the following code to perform the task:

```
    # Steps:
    #  1. Put gripper around the knob of the dial
    #  2. Turn the knob
    # We need to put the gripper around the knob of the dial before we can turn
    # it.
    if check("the robot's gripper is not around the knob of the dial"):
        robot.move_gripper("around the knob of the dial", close_gripper=True)
    # Once the gripper is lined up with the knob, we can just turn the knob.
    if check("the robot's gripper is around the knob of the dial"):
        robot.move_gripper("to the right")
```