

The program should be the following:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull open the drawer
    # Put the robot's gripper roughly around the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the gripper is near the drawer handle, we can pull open the drawer.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle")
```