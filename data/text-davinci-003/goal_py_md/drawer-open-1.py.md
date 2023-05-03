

Then provide your solution:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull open the drawer
    # If the robot's gripper is not near the drawer handle, we should move the
    # gripper to the left of the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # Once the gripper is near the drawer handle, pull the drawer open.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("pull open the drawer")
```