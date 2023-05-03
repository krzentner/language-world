# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench peg")
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is not near the disassemble target"):
        robot.reach("to disassemble goal")
    if check("the robot's gripper is almost vertically aligned with disassemble target and the robot's gripper is open"):
        robot.put("gripper around disassemble target")
    if check("the robot's gripper is vertically aligned with the disassemble target and the grip is tight"):
        robot.pull("wrench off the peg")