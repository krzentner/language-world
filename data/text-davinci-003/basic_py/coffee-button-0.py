
    if check("the robot's gripper is not near the button"):
        robot.put("gripper near button")
    if check("the robot's gripper is near the button"):
        robot.push("the button")