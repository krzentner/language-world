

Solution:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Push gripper into handle
    #  3. Pull handle up
    # First, move the robot's gripper roughly above the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the robot's gripper is near the handle but not trying to grab it, move
    # the gripper down to the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is not trying to grab the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Once the gripper is around the handle and closed, push down on the handle
    # to hold it in place while we pull it up.
    if check("the robot's gripper is vertically aligned with the handle and the gripper is closed"):
        robot.move_gripper("above the handle")
    # As long as the gripper is above the handle, we can pull it up.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("horizontally aligned with the handle")
```