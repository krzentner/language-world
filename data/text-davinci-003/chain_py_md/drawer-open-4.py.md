
Here is the code:
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
    # If the gripper isn't around the drawer handle, put it around the drawer handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # If the gripper is near the drawer handle and closed, we should be able to
    # pull the drawer open.
    if check("the robot's gripper is near drawer handle and the robot's gripper is closed"):
        robot.pull("drawer open")
```