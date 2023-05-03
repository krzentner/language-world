
    # Steps:
    #  1. Put gripper around wrench
    #  2. Pull wrench off peg
    # As long as the wrench is around the peg, we can grab it by moving gripper
    # around it.
    if check("the robot's gripper is not around wrench and the wrench is around peg"):
        robot.grab("wrench")
    # Once the gripper is around the wrench, we can pull it off the peg.
    if check("the robot's gripper is around wrench"):
        robot.pull("wrench off peg")