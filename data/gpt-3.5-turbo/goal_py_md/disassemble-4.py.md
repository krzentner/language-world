# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper near the wrench
    #  2. Grab the wrench
    #  3. Pull the wrench off the peg
    # First, put the gripper near the wrench.
    if check("the robot's gripper is not almost vertically aligned with the wrench and the wrench is not in the gripper"):
        robot.move_gripper("near the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # If the gripper is around the wrench, pull the wrench off the peg.
    if check("the robot's gripper is around wrench"):
            robot.move_gripper("above the peg")