

And end with:

```
    # Once the gripper is around the drawer handle, we can just push the drawer
    # closed.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("right of the drawer handle")
```

Steps: 
1. Put gripper left of the drawer handle
2. Start pushing against the drawer handle to close the drawer
3. Push the drawer closed harder

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Start pushing against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # If the drawer handle is right of the robot's gripper, we should move the
    # gripper near the drawer handle to start pushing
    if check("the robot's gripper is right of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # If the robot's gripper is near the drawer handle we can probably slide the
    # drawer close now by moving the gripper right.
    if check("the drawer handle is right of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle")
    # If the robot's gripper is starting to be in front of the drawer handle,
    # push harder.
    if check("the robot's gripper is near the drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle")
```