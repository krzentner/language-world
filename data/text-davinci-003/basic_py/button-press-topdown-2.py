
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("button down")