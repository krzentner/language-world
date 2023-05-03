# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench back and forth to loosen it
    #  4. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench yet, move it close and close the
    # gripper to grab the wrench.
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Now that the gripper is around the wrench, move it back and forth over the
    # peg to loosen the wrench.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("back and forth over the peg", close_gripper=True)
    # Once the wrench is loose, pull it off the peg.
    if check("the wrench is loose"):
        robot.move_gripper("away from the peg")