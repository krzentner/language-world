
    if check("the robot's gripper is not vertically aligned with the door dial"):
        robot.put("gripper above door dial")
    if check("the robot's gripper is vertically aligned with the door dial and the robot's gripper is not around the door dial"):
        robot.drop("gripper around door dial")
    if check("the robot's gripper is around the door dial"):
        robot.turn("door dial right")