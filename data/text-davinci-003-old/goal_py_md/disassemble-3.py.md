

Steps:
1. Put gripper above the wrench
2. Grab the wrench with the gripper
3. Pull the wrench up

# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench up
    # First, move the gripper roughly above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the gripper is around the wrench, pull the wrench up.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("above the peg")