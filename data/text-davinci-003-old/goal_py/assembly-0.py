
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Clamp the wrench around the peg
    #  3. Tighten the wrench around the peg
    # First, we need to line up the robot's gripper with the wrench as seen from
    # above.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Now that the gripper is above the wrench, we can clamp the wrench around
    # the peg.
    if check("the robot's gripper is above the wrench and the wrench is not almost vertically aligned with the peg"):
        robot.move_gripper("almost vertically aligned with the peg")
    # Once the wrench is clamped around the peg, we can tighten it by pushing
    # down from the side.
    if check("the wrench is almost vertically aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")