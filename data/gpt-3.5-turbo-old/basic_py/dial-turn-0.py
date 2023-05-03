if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")