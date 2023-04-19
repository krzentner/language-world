
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is above the handle and the robot's gripper is closed"):
        robot.push("down on handle")