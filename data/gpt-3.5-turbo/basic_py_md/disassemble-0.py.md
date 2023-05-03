# disassemble: pull the wrench off the peg
def disassemble(robot):
    if check("the robot's gripper is not aligned with the wrench"):
        robot.move("gripper to left of wrench")
    if check("the robot's gripper is aligned with the wrench and the robot's gripper is not grabbing anything"):
        robot.grab("wrench")
    if check("the robot's gripper is grabbing the wrench and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    if check("the wrench is horizontally aligned with the peg"):
        robot.pull("wrench off peg")