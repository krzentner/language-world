

# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above the wrench handle
    #  2. Grab the wrench handle with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench handle so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the wrench handle"):
        robot.place("gripper above wrench handle")
    # If the gripper isn't around the wrench handle, put it around it.
    if check("the robot's gripper is not around wrench handle and the robot's gripper is open"):
        robot.drop("gripper around wrench handle")
    # As long as the gripper is still around the wrench handle, pull it off the
    # peg.
    if check("the robot's gripper is around wrench handle"):
        robot.pull("wrench off peg")