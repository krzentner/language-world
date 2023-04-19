Here's your code for `door-close` task:

```
# door-close: push the door closed to the target location
# def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is backward aligned with the door handle"):
        robot.push("door closed")
``` 

This code will check if the robot's gripper is near the door handle or not. If it's not near, it will grab the handle. Then it checks if the robot's gripper is backward aligned with the door handle or not. If it's backward aligned, it will push the door closed.