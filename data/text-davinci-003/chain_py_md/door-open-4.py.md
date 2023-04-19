

The program should look like this:

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper roughly above door handle, so that we don't bump 
    # it while trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.drop("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle, it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("the door open")
```