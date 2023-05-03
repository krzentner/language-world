
    if check("the robot's gripper is not above the dial "):
        robot.move("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is not near the dial"):
        robot.move("gripper near dial")
    if check("the robot's gripper is near the dial"):
        robot.turn("dial")