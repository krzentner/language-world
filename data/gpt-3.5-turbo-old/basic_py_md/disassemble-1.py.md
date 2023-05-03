# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is not left of the wrench"):
        robot.move("gripper to left of wrench")
    if check("the robot's gripper is not around the wrench"):
        robot.grab("the wrench")
    if check("the robot's gripper is forward aligned with the peg and the wrench is not vertically aligned with the peg"):
        robot.align("wrench to peg")
    if check("the wrench is vertically aligned with the peg"):
        robot.pull("wrench off the peg")