

Solution: 

```
# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not aligned with the peg"):
        robot.grab("wrench")
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is aligned with the peg"):
        robot.pull("wrench from the peg")