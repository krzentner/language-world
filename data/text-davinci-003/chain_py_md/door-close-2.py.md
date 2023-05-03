

Then fill in the code like this:

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper close to the door handle
    #  2. Push the door closed
    # We need to move the gripper near the door handle to start pushing
    if check("the robot's gripper is not close to the door handle"):
        robot.put("gripper close to the door handle")
    # If the robot's gripper is near the door handle, the robot will probably be
    # able to push it closed.
    if check("the robot's gripper is close to the door handle"):
        robot.push("door closed")
```