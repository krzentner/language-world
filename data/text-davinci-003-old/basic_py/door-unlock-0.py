
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above the dial")
    if check("the robot's gripper is touching the dial"):
        robot.turn("dial clockwise")
    if check("the robot's gripper is still touching the dial"):
        robot.turn("dial around one time")