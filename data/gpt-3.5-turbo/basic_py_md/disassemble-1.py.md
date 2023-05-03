# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not near the wrench"):
        robot.grab("wrench handle")
    if check("the wrench is attached to the peg"):
        robot.pull("wrench off the peg")
    if check("the robot's gripper is holding the wrench"):
        robot.place("wrench in container")