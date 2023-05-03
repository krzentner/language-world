if check("the robot's gripper is not near the dial"):
        robot.grab("dial")
    if check("the robot's gripper is holding the dial and the robot is not in front of the dial"):
        robot.move("in front of dial")
    if check("the robot's gripper is in front of the dial and the dial is not at the desired setting"):
        robot.turn("dial to desired setting")