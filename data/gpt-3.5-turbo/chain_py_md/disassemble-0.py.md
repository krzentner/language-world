# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the gripper is not around the wrench, put it around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # Once the gripper is around the wrench, we can pull it off the peg by
    # lifting the gripper.
    if check("the robot's gripper is around wrench and the wrench is on the peg"):
        robot.pull("the gripper up to remove wrench from peg")