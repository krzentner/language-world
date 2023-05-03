

Then continue with the following code:

```
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Start pushing against the drawer handle to close the drawer
    #  3. Push the drawer closed harder
    # If the the drawer handle is right of the robot's gripper, we should move the
    # gripper near the drawer handle to start pushing
    if check("the drawer handle is right of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move("gripper to left of drawer handle")
    # If the robot's gripper is near the drawer handle we can probably slide the
    # drawer closed now by moving the gripper right.
    if check("the robot's gripper is near the drawer handle"):
        robot.slide("drawer right")
    # If the robot's gripper is starting to be in front of the drawer handle,
    # push harder.
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer right harder")
```