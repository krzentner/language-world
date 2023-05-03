

```
# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is above the peg and the robot's gripper is not around the wrench"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is around the wrench and the wrench is not vertically aligned with the peg"):
        robot.pull("wrench up from peg")
    if check("the wrench is vertically aligned with the peg"):
        robot.pull("wrench away from peg")
```