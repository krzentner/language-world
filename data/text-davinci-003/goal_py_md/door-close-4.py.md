

Then proceed with the code:

```
# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    if check("the robot's gripper is not near door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, push the door closed.
    if check("the robot's gripper is near door handle"):
        robot.move_gripper("around the door handle")
    # If the door is near the target location, slow down the robot's movements
    # so it does not crash into the wall.
    if check("the door is near the target location"):
        robot.move_gripper("slowly towards the target location")
```