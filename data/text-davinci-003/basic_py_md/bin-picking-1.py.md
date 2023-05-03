

Solution:

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.grab("cube")
    if check("the robot's gripper is forward aligned with the cube and the cube is not horizontally aligned with bin"):
        robot.align("cube to bin")
    if check("cube is horizontally aligned with bin"):
        robot.insert("cube into bin")
```