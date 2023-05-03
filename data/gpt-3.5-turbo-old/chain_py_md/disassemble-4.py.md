# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Slide the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above the wrench")
    # If the wrench isn't in the gripper yet, grab it.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.drop("gripper around the wrench")
        robot.close("gripper around the wrench")
    # If the wrench is in the gripper, slide it off the peg.
    if check("the wrench is in the robot's gripper"):
        robot.slide("the wrench off the peg")