# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Twist the dial
    # To turn the dial, the gripper first needs to be positioned around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, turn the dial.
    if check("the robot's gripper is around dial"):
        robot.twist("the dial")