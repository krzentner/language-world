# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench handle"):
        robot.put("gripper above wrench handle")
    if check("the robot's gripper is vertically aligned with the wrench handle and the robot's gripper is not around wrench handle"):
        robot.put("gripper around wrench handle")
    if check("the robot's gripper is around wrench handle"):
        robot.pull("wrench off the peg")