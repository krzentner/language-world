
    # Steps:
    #  1. Put gripper in front of the dial
    #  2. Turn the dial
    #  3. Repeat until the door is unlocked
    # We don't have to be very precise here, so putting the gripper in front of
    # the dial should do.
    if check("the robot's gripper is not forward aligned with dial"):
        robot.move_gripper("forward aligned with the dial")
    # Now just turn the dial and repeat until the door is unlocked.
    if check("the robot's gripper is forward aligned with dial"):
        robot.move_gripper("clockwise")