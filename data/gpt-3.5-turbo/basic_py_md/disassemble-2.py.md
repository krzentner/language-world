# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    if check("wrench is horizontally aligned with the peg"):
        robot.pull("wrench off the peg")