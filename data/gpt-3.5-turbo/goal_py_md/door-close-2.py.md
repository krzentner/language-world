Here's the program to perform the `door-close` task using the robot's gripper:

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed to the target location
    # First, put the gripper around the door handle.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # If the gripper is around the handle, push the door closed to the target
    # location.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("vertically aligned with the target location")
```

This program lines up the gripper with the door handle before pushing the door closed to the target location.