```
# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper mostly around door handle
    #  2. Push the door closed
    # First, put the gripper mostly around the door handle.
    if check("the robot's gripper is not mostly around door handle"):
        robot.move_gripper("mostly around the door handle")
    # Then, push the door closed towards the target location.
    if check("the robot's gripper is mostly around door handle"):
        robot.move_gripper("near the target location")
```