# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Align the wrench to the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the wrench isn't in the gripper, grab it.
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # If the wrench is not roughly aligned with the peg, align it.
    if check("the wrench is not roughly aligned with the peg"):
        robot.place("wrench rough alignment with the peg")
    # Once the wrench is roughly aligned with the peg, wrap it around the peg.
    if check("the wrench is roughly aligned with the peg"):
        robot.wrap("wrench around the peg")