

Then add the code below to complete the program:

```
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a short object, check if the gripper is lined up with
    # it from the side instead of from the top.
    if check("handle is not left of the robot's gripper and handle is not side-aligned with the robot's gripper"):
        robot.move_gripper("side aligned with the handle", close_gripper=True)
    # As long the gripper is still around the handle, pull it up.
    if check("the robot's gripper is side aligned with the handle"):
        robot.move_gripper("above the handle")
```