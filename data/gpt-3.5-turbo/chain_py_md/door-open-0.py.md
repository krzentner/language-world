Here's the program to perform the `door-open` task:

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Pull open the door
    # To open the door, we need to grab onto the door handle with the gripper.
    if check("the robot's gripper is not around door handle"):
        robot.grab("door handle")
    # Once we're holding onto the door handle, we can pull it to open the door.
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")
```

This function assumes that the robot has a door handle to grab onto. If the door doesn't have a handle, the function may need to be modified or a different function could be created to push the door open from its edges instead.