

Your program should go here:

```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.put("gripper near door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.grab("door handle")
    if check("the robots gripper is around door handle"):
        robot.pull("door open")
```