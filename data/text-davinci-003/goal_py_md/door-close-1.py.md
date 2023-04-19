

Steps:
1. Put gripper near the door handle
2. Push the door closed

```
# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    if check("the robot's gripper is not near door handle"):
        robot.move_gripper("near the door handle")
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("left or right of the door handle")