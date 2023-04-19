# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not near the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper near dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.align("gripper to dial")
    if check("the robot's gripper is aligned with the dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    if check("the robot's gripper is closed around the dial"):
        robot.turn("the dial")