

Then write the code:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper close to handle
    #  2. Grab and pull handle up
    # First, we just need to move the robot's gripper close to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is close to the handle, grab it and pull it up.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
```