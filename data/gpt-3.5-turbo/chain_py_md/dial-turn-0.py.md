# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper close to the dial
    #  2. Grab the dial
    #  3. Turn the dial
    # First, move the gripper close to the dial.
    if check("the robot's gripper is not close to the dial"):
        robot.move("gripper to dial")
    # Once the gripper is close to the dial, grab it.
    if check("the robot's gripper is close to the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    # Now that the gripper is around the dial, turn it.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")