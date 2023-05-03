

Then write your code:

```
# box-close: pick up the box lid and place it on the box
def box_close(robot): 
    if check("the robot's gripper is not above box lid and the robot's gripper is open"):
        robot.put("gripper above box lid")
    if check("the robot's gripper is above box lid and the robot's gripper is open"):
        robot.drob("gripper around box lid")
    if check("the robot's gripper is near the box lid and the robot's gripper is closed"):
        robot.align("box lid to box")
    if check("the robot's gripper is aligned with the box and the box lid is below the robot's gripper"):
        robot.push("place box lid onto box")
```