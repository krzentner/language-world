# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial
    # The gripper needs to be put around the dial before it can be turned.
    if check("the robot's gripper is not around the dial"):
        robot.grab("dial")
    # Once the gripper is around the dial, turn the dial.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")