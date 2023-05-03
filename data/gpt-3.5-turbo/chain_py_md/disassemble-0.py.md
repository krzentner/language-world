# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench to the left until it comes off the peg
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("wrench is not in the robot's gripper"):
        robot.grab("wrench")
    if check("the robot's gripper is not positioned to the left of the wrench"):
        robot.move("gripper to the left of wrench")
    if check("the wrench is still attached to the peg"):
        robot.pull("wrench to the left")