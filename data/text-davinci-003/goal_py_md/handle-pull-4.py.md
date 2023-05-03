

The robot needs to use its gripper to pull the handle up.

First, the robot needs to place its gripper above the handle so that it can grab it.

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Step:
    #  1. Put gripper above the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
```

Once the gripper is above the handle, the robot can grab the handle by closing its gripper around it.

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Step:
    #  1. Put gripper above the handle
    #  2. Grab the handle with gripper
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the gripper is vertically aligned, grab it by closing the gripper.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not closed"):
        robot.gripper_close()
```

Finally, the robot needs to pull the handle up by moving its gripper.

```
# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with gripper
    #  3. Pull the handle up with the gripper
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the gripper is vertically aligned, grab it by closing the gripper.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not closed"):
        robot.gripper_close()
    # If the gripper is closed, pull the handle up with the gripper.
    if check("the robot's gripper is closed"):
        robot.move_gripper("above the handle")
```