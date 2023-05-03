

Steps: 
1. Put gripper around the drawer handle
2. Push the gripper towards the drawer
3. Push harder with the gripper

```# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper around the drawer handle
    #  2. Push the gripper towards the drawer
    #  3. Push harder with the gripper

    # First, put the gripper around the drawer handle.
    if check("the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Then, push the gripper towards the drawer.
    if check("the robot's gripper is not pushing against the drawer"):
        robot.move_gripper("towards the drawer")
    # If the gripper is starting to push against the drawer, push harder to close
    # the drawer.
    if check("the robot's gripper is pushing against the drawer"):
        robot.move_gripper("towards the drawer", close_gripper=True)
```