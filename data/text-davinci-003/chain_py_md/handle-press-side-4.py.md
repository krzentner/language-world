

Fill in the body of the code:

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Push down on the handle
    # First, put the gripper beside the handle in order to be able to push it.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.place("gripper to the side of handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle")
```