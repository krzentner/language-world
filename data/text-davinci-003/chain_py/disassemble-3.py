
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Drop gripper around wrench
    #  3. Pull wrench off peg
    # This operation is fairly straight forward - we just need to move the
    # gripper to the wrench and grip it, then pull it off the peg.
    # First, move the gripper above the wrench.
    if check("the robot's gripper is not above wrench"):
        robot.put("gripper above wrench")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the wrench and the robot's gripper is open"):
        robot.put("gripper around wrench")
    # As long as the gripper is still around the wrench and the wrench hasn't
    # come off the peg yet, keep pulling.
    if check("the robot's gripper is around the wrench and the wrench is stuck on the peg"):
        robot.pull("wrench off peg")