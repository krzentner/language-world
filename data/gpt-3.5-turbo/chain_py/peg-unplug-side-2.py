# Steps:
    #  1. Put the gripper around the peg
    #  2. Move the gripper to the side to start pulling the peg
    #  3. Pull the peg out
    # First, put the gripper around the peg.
    if check("the gripper is not around the peg"):
        robot.place("gripper around peg")
    # If the gripper is not left of the peg, move it left to start pulling the
    # peg out.
    if check("the gripper is not left of the peg"):
        robot.move("gripper to the left of the peg")
    # Once the gripper is left of the peg, we can pull the peg out to the left.
    if check("the gripper is left of the peg"):
        robot.pull("peg out to the left")