

Solution:

```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around the door handle"):
        robot.grab("around door handle")
    if check("the robot's gripper is around the door handle"):
        robot.pull("away from the door")