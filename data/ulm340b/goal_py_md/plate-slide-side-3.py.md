

To help you get started, I'll let you use my solution to the `drawer-open` task:

```
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")
```

Please use it to help you complete the following instructions:
```
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # REPLACE LINE 1: First, put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # REPLACE LINE 2: Once the gripper is lined up above the drawer handle, we should be able to
    # REPLACE LINE 2: grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # REPLACE LINE 3: Once the gripper is around the drawer handle, we can just pull the drawer
    # REPLACE LINE 3: open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the