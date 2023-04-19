
    # Steps:
    #  1. Put gripper in front of the dial
    #  2. Turn the dial
    # Put the robot's gripper in front of the dial
    if check("the robot's gripper is not forward aligned with the dial"):
        robot.move_gripper("forward aligned with the dial")
    # Now that the gripper is in front of the dial, move the gripper around it
    # to turn the dial.
    if check("the robot's gripper is forward aligned with the dial"):
        robot.move_gripper("around the dial")