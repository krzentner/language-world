# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    # 1. Put gripper above the wrench
    # 2. Grab the wrench with the gripper
    # 3. Move the wrench to the right to disengage it from the peg
    # 4. Move the gripper up to remove the wrench from the peg
    # First, put the gripper roughly above the wrench, so we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is near the wrench and closed, move the wrench to the right to disengage it from the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("right of the wrench")
    # Once the wrench is disengaged from the peg, move the gripper up to remove the wrench.
    if check("the wrench is disengaged from the peg"):
        robot.move_gripper("above the peg")