
    # Steps:
    #  1. Put gripper above or at level with the wrench
    #  2. Pull the wrench away from the peg
    #  3. Pull the wrench straight up when it's free
    # We want to keep the wrench from going vertical, so we start by putting the
    # gripper above or at the same height as the wrench.
    if check("the robot's gripper is not at the same level as the wrench"):
        robot.put("gripper at same level as wrench")
    # Once the gripper is in the right location, we can try to pull the wrench
    # away from the peg.
    if check("the robot's gripper is at the same level as the wrench"):
        robot.pull("wrench away from peg")
    # If the wrench is far enough away from the peg, it might be time to pull it
    # straight up.
    if check("the wrench not touching the peg"):
        robot.pull("wrench straight up")