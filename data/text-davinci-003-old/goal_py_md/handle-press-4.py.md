

Steps:
1. Put gripper above handle
2. Drop gripper around handle
3. Push down on handle

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down on handle
    # First, put the gripper roughly above the handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is near the handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above the handle and the robot's gripper is closed"):
        robot.move_gripper("near the handle")
    # Once the gripper is around the handle, push the handle down.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("downwards on the handle")
```