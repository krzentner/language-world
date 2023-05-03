
    if check("the robot's gripper is not above the dial"):
        robot.place("gripper to left side of dial")
    if check("the robot's gripper is above the dial"):
        robot.turn("dial to unlock")