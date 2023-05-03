# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    # 1. Move gripper to the dial
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # 2. Grab the dial
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.grab("dial")
    # 3. Turn the dial
    if check("the robot's gripper is around the dial"):
        robot.turn("the dial")