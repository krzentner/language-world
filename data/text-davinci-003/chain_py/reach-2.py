
    # Steps:
    #  1. Move robot arm to above target
    #  2. Rotate robot arm to align with target
    #  3. Open hand
    # We need to move the robot arm to the right position first.
    # This is the same no matter what the robot is doing.
    # Move the robot arm up or down to get it above the target.
    if check("the robot's arm is not vertically aligned with the target"):
        robot.move("arm above target")
    # Once the robot arm is at roughly the right height, rotate it to align it
    # with the target.
    if check("the robot's arm is above the target but not aligned with the target"):
        robot.rotate("arm to align with target")
    # If the robot arm is roughly aligned with the target, open the hand.
    # This will allow the robot to reach out and grab the target.
    if check("the robot's arm is almost aligned with the target"):
        robot.open("hand")