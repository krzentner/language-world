

Then complete the program:

```
# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("near the handle")
```