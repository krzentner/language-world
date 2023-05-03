# dial-turn: turn the dial
# def dial_turn(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("the gripper to the dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not touching the dial"):
        robot.grab("the dial")
    if check("the robot's gripper is touching the dial"):
        robot.rotate("the dial clockwise") # adjust direction as needed
    if check("the dial is at the desired position"):
        robot.release("the dial")