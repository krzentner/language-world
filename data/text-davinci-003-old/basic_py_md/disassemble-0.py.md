

```
# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not near the peg"):
        robot.reach("to the peg")
    if check("the robot's gripper is near the peg and the wrench is not around the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench"):
        robot.pull("wrench off peg")
```