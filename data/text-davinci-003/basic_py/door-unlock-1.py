
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is not near dial and the robot's gripper is open"):
        robot.grab("dial with gripper")
    if check("the robot's gripper is near dial"):
        robot.turn("dial to unlock")