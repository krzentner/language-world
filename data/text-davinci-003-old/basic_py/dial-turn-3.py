
    if check("the robot's gripper is not above the dial"):
        robot.place("gripper above dial")
    if check("the robot's gripper is above the dial"):
        robot.turn("dial")