
    if check("the robot's gripper is not aligned with the dial"):
        robot.grip("dial")
    if check("the robot's gripper is aligned with the dial and the dial is in the incorrect position"):
        robot.turn("dial to desired position")