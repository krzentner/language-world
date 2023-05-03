# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the desired position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # If the gripper is around the dial, turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to desired position")