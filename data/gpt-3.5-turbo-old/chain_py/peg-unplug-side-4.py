# Steps:
    #  1. Put the gripper around the top of the peg
    #  2. Pull upwards to remove the peg from the hole
    # First, put the gripper around the top of the peg.
    if check("the robot's gripper is not around the top of the peg"):
        robot.grab("top of the peg")
    # If the gripper is around the top of the peg, pull upwards to remove the
    # peg from the hole.
    if check("the robot's gripper is around the top of the peg"):
        robot.pull("the peg out")