

Answer:

```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not holding the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is holding the wrench and the peg is not horizontally aligned with the robot's gripper"):
        robot.align("peg to gripper")
    if check("the peg is horizontally aligned with the robot's gripper and the robot's gripper is not around the peg"):
        robot.drop("gripper around peg")
```