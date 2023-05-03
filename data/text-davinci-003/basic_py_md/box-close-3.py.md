

Solution:

```
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    if check("the robot's gripper is not around the box lid"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is near the box lid and robot's gripper is open"):
        robot.close("gripper around box lid")
    if check("the robot's gripper is above the box lid and robot's gripper is closed"):
        robot.put("box lid on box")
```