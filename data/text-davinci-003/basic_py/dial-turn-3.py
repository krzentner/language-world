
    if check("the robot's gripper is not near the dial"):
        robot.grab("dial")
    if check("the robot's gripper is near the dial"):
        robot.turn("dial")