

Then write the following code:

```
if check("the robot's gripper is not above the wrench"):
    robot.put("gripper above wrench")
if check("the robot's gripper is above the wrench"):
    robot.grab("wrench")
if check("the robot's gripper is not above the peg and the robot's gripper is not forward aligned with the peg"):
    robot.put("gripper forward aligned with peg")
if check("the robot's gripper is forward aligned with the peg and the robot's gripper is not vertical aligned with the peg"):
    robot.align("gripper with peg")
if check("the robot's gripper is vertical aligned with the peg"):
    robot.pull("wrench off peg")
```