if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")