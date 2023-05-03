# Steps:
    #  1. Align the gripper with the dial
    #  2. Turn the dial clockwise
    #  3. Stop turning when the lock clicks open
    # Put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Try turning the dial a little bit clockwise.
    if check("the dial is not turned clockwise and the robot's gripper is around the dial"):
        robot.move_gripper("clockwise a little bit")
    # Keep turning the dial until the lock clicks open.
    if check("the lock has not clicked open yet"):
        robot.move_gripper("clockwise")