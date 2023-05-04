Here's the complete program to perform the `drawer-open` task using the provided code:

```
# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("drawer open")
```

The program checks if the gripper is in the correct position and then uses the robot's `put` and `pull` methods to grab and pull the drawer open.