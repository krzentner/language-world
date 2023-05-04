

Then, write a few lines of code that make the robot perform the drawer-close task. 
The first few lines are given below to get you started. 
You will be allowed to use each command up to **10** times.

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Grab the drawer handle
    #  3. Push the drawer close

    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")

    # 1. Put gripper above drawer handle

    # If the gripper isn't around the drawer handle, drop it around the handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.move_gripper("around the drawer handle", close_gripper=True)

    # 2. Grab the drawer handle

    # Push the drawer handle closed.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("right of the drawer handle")

    # 3. Push the drawer close
```

## Answer

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Grab the drawer handle
    #  3. Push the drawer close

    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")

    # 1. Put gripper above drawer handle

    # If the gripper isn't around the drawer handle, drop it around the handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.move_gripper("around the drawer handle", close_gripper=True)

    # 2. Grab the drawer handle

    # Push the drawer handle closed.
    if check("the robot's gripper is around drawer