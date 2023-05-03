# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("the gripper to the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not aligned with the dial"):
        robot.align("the gripper with the dial")
    if check("the robot's gripper is aligned with the dial and the robot's gripper is not around the dial"):
        robot.drop("the gripper around the dial")
    if check("the robot's gripper is around the dial"):
        robot.rotate("the dial to the desired position")