

Solution

```
# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    if check("the wrench is not slightly away from the robot's gripper and the robot's gripper is open"):
        robot.grab("wrench")
    if check("the wrench is slightly away from the robot's gripper and the robot's gripper is closed"):
        robot.pull("wrench away from peg")
    if check("the robot's gripper is not empty"):
        robot.open("gripper to release wrench")