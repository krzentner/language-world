Here's the program to perform the `door-open` task:

```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")
```

This program first checks if the robot's gripper is not almost vertically aligned with the door handle. If that's the case, it moves the gripper above the door handle using the `robot.put()` function. Next, it checks if the gripper is almost vertically aligned with the door handle and the gripper is open. If that's the case, it moves the gripper around the door handle using the same `robot.put()` function. Finally, it checks if the gripper is vertically aligned with the door handle. If that's the case, it pulls the door open using the `robot.pull()` function.