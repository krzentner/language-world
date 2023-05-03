

Solution:
```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door
    # handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper, we can push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")
```