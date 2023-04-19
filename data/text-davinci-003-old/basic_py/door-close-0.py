
    if check("the robot's gripper is not near the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is near the door handle and the door is open"):
        robot.push("door closed")
    if check("the robot's gripper is near the door handle and the door is closed"):
        robot.pull("door closed further")