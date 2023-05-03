

Then, fill in the following code to complete the task:

```
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.align("puck to goal")
    if check("the robot's gripper is forward aligned with the puck"):
        robot.insert("puck into goal")
```