
    # Steps:
    #  1. Put gripper above lock
    #  2. Line up the gripper with the dial
    #  3. Turn the dial
    # The robot needs to line up with the dial from above.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Once the gripper is lined up with the dial, we can turn it by moving the
    # gripper in a circle.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("round the dial")