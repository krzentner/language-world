
    # Steps:
    #  1. Put the gripper right of the peg
    #  2. Start to pull the peg out
    #  3. Pull the peg harder
    # First, make sure the side of the peg that is sticking out of the hole is
    # right of the gripper.
    if check("the side of the peg that is sticking out of the hole is not right of the robot's gripper"):
        robot.move("gripper to the right of the peg")
    # As long as the gripper is still lined up with the peg from the side, start
    # to pull it out.
    if check("the robot's gripper is side aligned with the peg"):
        robot.pull("peg out")
    # If the peg isn't moving, it's probably stuck, so pull harder.
    if check("the peg is not coming out"):
        robot.pull("peg out harder")