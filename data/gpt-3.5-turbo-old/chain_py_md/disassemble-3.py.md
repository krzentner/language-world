# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the gripper away from the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with 
    # it from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.grab("wrench")
    # Pull the wrench away from the peg while keeping it in the gripper's grasp.
    if check("the wrench is held by the gripper and the wrench is still on the peg"):
        robot.pull("wrench off the peg")
    # Drop the wrench after removing it from the peg.
    if check("the wrench is no longer on the peg"):
        robot.drop("wrench")