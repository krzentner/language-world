
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.turn("dial until lock opens")