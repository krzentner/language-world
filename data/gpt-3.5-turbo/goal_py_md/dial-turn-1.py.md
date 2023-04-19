# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, put the robot's gripper above the dial to avoid hitting it when turning it.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # Once the gripper is above the dial, move it down to grasp the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Now that the gripper is around the dial, turn the dial in the desired direction.
    if check("the robot's gripper is around the dial"):
        robot.turn_dial()