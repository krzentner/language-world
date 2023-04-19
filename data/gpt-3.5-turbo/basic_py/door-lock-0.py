if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    if check("the dial is not aligned with the top of the robot's gripper"):
        robot.turn("dial to top aligned with gripper")
    if check("the top of the dial and the top of the robot's gripper are aligned"):
        robot.turn("dial to right")