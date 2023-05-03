

The program should be:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # If the gripper is left of the drawer handle, pull the drawer open by
    # moving the gripper right.
    if check("the robot's gripper is almost vertically aligned withe the drawer handle"):
        robot.pull("right")
        robot.move_gripper("right of the drawer")
```