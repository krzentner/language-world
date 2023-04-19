
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not near the dial and the dial is above the robot's gripper"):
        robot.put("gripper below dial")
    if check("the robot's gripper is near the dial"):
        robot.turn("dial")