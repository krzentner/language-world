

## Solution 

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is aligned with the peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near the peg"):
        robot.pull("peg to the side of the hole")
    if check("the robot's gripper is above the hole and the peg is aligned with the hole"):
        robot.push("peg into the hole")
```