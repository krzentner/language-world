

Then, finish the program:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put the gripper in front of the drawer handle
    #  2. Push the drawer closed
    # Put the gripper in front of the drawer handle by moving it above it.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up with the drawer handle, we can just push the
    # drawer closed.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.push("back against drawer")
```