

Here is the program you asked for: 

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
    # If the gripper isn't around the drawer handle, put it around the drawer
    # handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # As long as the gripper is still lined up with the drawer handle, keep
    # pulling it open.
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")
```