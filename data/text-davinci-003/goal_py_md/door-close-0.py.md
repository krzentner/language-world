

Then follow the steps:
1. Put gripper around the door handle
2. Push the door closed

```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Push the door closed
    # Move the gripper around the door handle before pushing the door closed. 
    if check("the robot's gripper is not around the door handle"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # If the gripper is around the door handle, we can push the door closed.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("left of the door handle")
```