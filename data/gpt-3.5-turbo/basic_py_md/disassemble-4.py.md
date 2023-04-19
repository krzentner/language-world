# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not near the wrench and the robot's gripper is open"):
        robot.put("the gripper near the wrench")
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.grab("the wrench")
    if check("the robot's gripper is around the wrench"):
        robot.pull("the wrench off the peg")