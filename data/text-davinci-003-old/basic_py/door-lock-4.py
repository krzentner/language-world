
    if check("the robot's gripper is not vertially aligned with the door lock dial"):
        robot.put("gripper above door lock dial")
    if check("the robot's gripper is vertically aligned with the door lock dial"):
        robot.turn("dial until it locks")