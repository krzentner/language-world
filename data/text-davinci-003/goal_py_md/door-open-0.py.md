

We need to first put the gripper above the door handle before we can grab it.

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put the gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # Put the gripper above the door handle
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Now, we can pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
```