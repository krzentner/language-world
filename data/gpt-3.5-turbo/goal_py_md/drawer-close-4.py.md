Here's the code to perform the task of closing a drawer:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Move gripper to the left of the drawer handle
    #  3. Push the drawer closed
    # Put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is above the drawer handle, move it to the left side of
    # the handle to prepare to push the drawer closed.
    if check("the robot's gripper is not left of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # Now that the gripper is in position, we can push the drawer closed.
    if check("the drawer is not fully closed"):
        robot.move_gripper("almost horizontally aligned with the drawer handle")
``` 

This function will put the gripper above the drawer handle, move it to the left of the handle, and then push the drawer closed. Note that we assume the drawer is fully open when this function is called.