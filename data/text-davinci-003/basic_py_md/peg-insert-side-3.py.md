

Solution:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above the peg")
    if check("the robot's gripper is not around the peg"):
        robot.drop("gripper around the peg")
    if check("the robot is aligned with the peg"):
        robot.rotate("clockwise")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around the peg")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.slide("the peg into the hole from the side")
```