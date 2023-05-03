

Then continue from there:

```
# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Line the gripper up with the door handle
    #  3. Push the door closed to the target location
    # If the robot's gripper is not near the door handle, move it to the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")

    # Once the gripper is near the door handle, align it with the door handle so that it can close the door.
    if check("the robot's gripper is not horizontally aligned with door handle"):
        robot.move_gripper("horizontally aligned with the door handle")

    # When the gripper is in the right spot, just push the door closed.
    if check("the robot's gripper is horizontally aligned with door handle"):
        robot.move_gripper("around the door handle")

```