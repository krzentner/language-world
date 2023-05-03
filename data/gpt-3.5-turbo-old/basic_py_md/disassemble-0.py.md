# disassemble: pull the wrench off the peg
# def disassemble(robot):
    if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is below the wrench"):
        robot.move("gripper to right of wrench")
    if check("the robot's gripper is near the wrench"):
        robot.grab("the wrench")
    if check("the robot's gripper is around the wrench"):
        robot.pull("the wrench off the peg")
    if check("the robot's gripper is holding the wrench"):
        robot.drop("the wrench")