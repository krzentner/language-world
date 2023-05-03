

Here's the program:

```
# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper in front of the door handle
    #  2. Push against the door handle to move the door
    #  3. Push the door closed more
    # First, we need to move the robot's gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the robot's gripper is near the door handle, we just need to push the
    # door closed a little to start the door moving.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("left of the door handle")
    # Once the door is moving, push harder.
    if check("the robot's gripper is horizontally aligned with the door handle"):
        robot.move_gripper("around the door handle")
    # Keep pushing until the door closes.
    if check("the door is not closed"):
        robot.move_gripper("around the door handle")
```