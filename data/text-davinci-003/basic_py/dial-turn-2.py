
    if check("the robot's gripper is not above dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above dial and the robot's gripper is open"):
        robot.grab("dial")
    if check("the robot's gripper is above dial and the robot's gripper is closed"):
        robot.turn("dial clockwise")