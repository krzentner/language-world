

The program should look like this:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # If the gripper isn't around the drawer handle, put it around the handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # If the drawer handle is aligned with the gripper as seen from in front, we
    # can pull the drawer open.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
```