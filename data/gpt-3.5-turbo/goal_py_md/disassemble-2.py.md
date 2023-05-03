# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Lift the wrench up and out of the hole
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't grabbed by the gripper, close the gripper around it.
    if check("the robot's gripper is above the wrench and the gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Once the wrench is grabbed by the gripper, lift it up and out of the hole.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("above the hole")