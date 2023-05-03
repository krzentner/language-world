
    # Steps:
    #  1. Line up the gripper with the dial
    #  2. Pull dial in the desired direction
    # First, line up the gripper with the dial.
    # We want to align the gripper with the dial from the front, not just above
    # it.
    if check("the robot's gripper is not forward aligned with dial"):
        robot.move_gripper("forward aligned with the dial")
    # Now that the gripper is lined up, just grab the dial and pull it in the
    # direction we want.
    if check("the robot's gripper is forward aligned with the dial and the robot's gripper is not around the dial"):
        robot.move_gripper("grab the dial")