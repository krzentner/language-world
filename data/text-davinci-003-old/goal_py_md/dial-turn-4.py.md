

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn the dial
    # First, move the robot's gripper to the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above dial")
    # Then, drop the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around dial")
    # Finally, start turning the dial by moving the gripper left or right.
    # Make sure to keep a tight grip on the dial!
if check("the robot's gripper is around the dial"):
    robot.move_gripper("left or right of dial")