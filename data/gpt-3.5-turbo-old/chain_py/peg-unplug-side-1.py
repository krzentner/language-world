# Steps:
    #  1. Put gripper around the peg
    #  2. Line the peg up with the hole
    #  3. Pull the peg out from the hole
    # First, put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the peg is not horizontally aligned with hole and the robot's gripper is forward aligned with the peg"):
        robot.align("peg to hole")
    # Once the gripper is lined up with the peg and the peg is aligned with the
    # hole, pull the peg out sideways.
    if check("the peg is horizontally aligned with the hole"):
        robot.pull("peg out from the hole")