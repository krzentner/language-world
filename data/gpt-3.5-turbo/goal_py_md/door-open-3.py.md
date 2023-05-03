Here's a program to perform the `door-open` task:

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Pull open the door
    # We need to put the gripper around the door handle before we can grab it.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("near the door handle", close_gripper=True)
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
```

This program should work assuming `check` is a function that checks if a condition is True and returns True or False, and `robot.move_gripper` is a function that moves the robot's gripper to a specified position and optionally closes the gripper (True for `close_gripper`).