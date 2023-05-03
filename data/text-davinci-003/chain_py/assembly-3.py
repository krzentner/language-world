
    # Steps:
    #  1. Pick up the wrench
    #  2. Put the wrench around the peg
    # First, pick up the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.grab("wrench")
    # As long as the robot has the wrench and the wrench isn't around the peg, put
    # it around the peg.
    if check("the robot has the wrench and the wrench is not around the peg"):
        robot.put("wrench around peg")