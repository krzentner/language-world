# Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Rotate wrench counterclockwise to loosen it
    #  4. Pull wrench off peg
    # First, put the gripper roughly above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, we should be able to drop it around
    # the wrench.
    if check("the robot's gripper is above wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If we have the wrench gripped, we can rotate it by a fixed amount to try
    # to loosen it.
    # We don't need to check the angle of the wrench after rotating, because
    # we're not trying to turn the bolt a specific amount.
    if check("the robot's gripper is around wrench"):
        robot.rotate("wrench counterclockwise")
    # Once the wrench is rotated, we can try to pull it off the peg.
    # If we want to make sure we don't just rotate the wrench back to where it
    # was, we could check that the gripper is not vertical. However, the angle
    # in that case would be sensitive to small movements, so we'll assume the
    # wrench is simply gripped tightly enough that it won't accidentally rotate
    # too much.
    if check("the robot's gripper is around wrench and the robot's gripper is not vertical to the peg"):  # could instead check the angle is not too small
        robot.pull("wrench off peg")