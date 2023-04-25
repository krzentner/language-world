

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # If the gripper is near the dial, we've probably trapped the dial and can
    # turn it.
    if check("the robot's gripper is near the dial and the dial is below the robot's gripper"):
        robot.move_gripper("clockwise")