
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around dial
    #  3. Turn dial to left or right
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    # Now that the gripper is lined up, just turn the dial.
    if check("the robot's gripper is vertically aligned with dial"):
        robot.move_gripper("horizontally aligned with the dial")