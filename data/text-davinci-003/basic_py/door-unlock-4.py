
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around the dial and the door is not unlocked"):
        robot.turn("dial clockwise")