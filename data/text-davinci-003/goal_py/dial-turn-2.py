
    # Steps:
    #  1. Put gripper close to the dial
    #  2. Put gripper around the dial
    #  3. Turn the dial
    # First, put the gripper close to the dial to make it easy to grab.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial and close the
    # gripper around it.
    if check("the robot's gripper is not around the dial and the robot's gripper is not closed"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can just turn the dial by using
    # the robot's gripper.
    if check("the robot's gripper is around the dial and the robot's gripper is closed"):
        robot.move_gripper("turn the dial")