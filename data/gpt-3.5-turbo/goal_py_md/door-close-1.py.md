Here is the code for the `door-close` task:

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Grab door handle
    #  3. Move gripper toward the door to close it
    # First, move the gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle", close_gripper=True)
    # If the gripper is around the door handle, we can start pushing the door
    # closed by moving the gripper towards the door.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("above the target location")
``` 

This code will move the robot's gripper near the door handle, grab the door handle, and then move the gripper towards the target location to push the door closed.