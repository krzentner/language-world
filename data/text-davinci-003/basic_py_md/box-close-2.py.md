

Then, write the code:

```
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    if check("the robot's gripper is open and the robot's gripper is above the box lid"):
        robot.drop("gripper around box lid")
    if check("the robot's gripper is closed and the robot's gripper is near the box lid"):
        robot.align("gripper above box")
    if check("the robot's gripper is closed and the robot's gripper is aligned with the box"):
        robot.place("box lid on box")
```