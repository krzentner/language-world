# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench's peg"):
        robot.put("gripper above wrench's peg")
    if check("the wrench is not in the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is near the wrench's peg"):
        robot.pull("the wrench off the peg")
    if check("the robot's gripper is not above the disassembly area"):
        robot.reach("disassembly area")
    if check("the robot's gripper is above the disassembly area"):
        robot.drop("the wrench")