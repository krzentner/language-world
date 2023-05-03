# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.grab("dial")
    if check("the dial is not turned to the correct position"):
        robot.turn("dial to desired position")