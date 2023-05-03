

Next, add the rest of the code:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper to the left of the drawer handle
    #  2. Start pushing against the handle to close the drawer
    #  3. Push the drawer closed harder
    # We need to put the gripper on the left of the drawer handle before we can
    # start pushing, because of the angle of the robot's gripper.
    if check("the drawer handle is left of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move("gripper to left of drawer handle")
    # Once the gripper is near the drawer handle, we can probably slide the
    # drawer close by moving the gripper to the right.
    if check("the robot's gripper is near drawer handle"):
        robot.slide("drawer right")
    # If the robot's gripper is starting to be in front of the drawer handle,
    # push harder.
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer right harder")
```