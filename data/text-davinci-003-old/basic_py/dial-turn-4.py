
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not above the dial"):
        robot.grab("dial")
    if check("the robot's gripper is above the dial"):
        robot.turn("dial to goal")