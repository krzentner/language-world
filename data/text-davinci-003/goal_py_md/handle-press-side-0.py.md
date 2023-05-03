

Steps: 
1. Put gripper above the handle
2. Push gripper sideways against the handle to push it down

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push gripper sideways against the handle to push it down
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    if check("the handle is not left of robot's gripper and the handle is not forward aligned with robot's gripper"):
        robot.move_gripper("forward aligned with the handle")
    # As long the handle isn't pressed down, move the gripper sideways to push
    # the handle down.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("left of the handle")
```