

Then complete the program:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # First, put the gripper roughly above drawer handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the drawer handle"):
        robot.place("gripper above drawer handle")
    # If the gripper isn't around the drawer handle, put it around the drawer handle.
    if check("the robot's gripper is not around drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # If the gripper is near the drawer handle and open, maybe we can grab it by closing
    # the gripper and pulling open the drawer.
    if check("the robot's gripper is near drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
        robot.pull("drawer open")
```