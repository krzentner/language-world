
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper down around the dial
    #  3. Turn the dial
    # As usual, we need to move the gripper above the dial before we can pick it up.
    if check("the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial")
    # When the gripper is almost lined up, close it to get a better grip.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("forward aligned with the dial", close_gripper=True)
    # With a good grip on the dial, we can just turn it.
    if check("the robot's gripper is forward aligned with dial and the robot's gripper is closed"):
        robot.move_gripper("near target angle")