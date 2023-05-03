

Then, add the code:

```
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle with the gripper
    #  3. Pull up to lift the handle
    # First, put the gripper above the handle so that we can grab it.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is not left of the gripper and the handle is not front-aligned
    # with the gripper, close the gripper around the handle.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # If the handle is left of the gripper, we should be able to pull the handle
    # up by pulling the gripper up.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("above the handle")
```