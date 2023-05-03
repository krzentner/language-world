# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not near dial"):
        robot.reach("to dial")
    if check("the robot's gripper is around dial knob"):
        robot.twist("to turn dial")