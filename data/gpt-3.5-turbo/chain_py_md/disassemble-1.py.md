# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is not in the gripper, grab it.
    if check("the robot's gripper is not around wrench"):
        robot.grab("wrench")
    # If the wrench is held by the gripper, pull it off the peg.
    if check("the wrench is attached to the peg"):
        robot.pull("wrench off peg")