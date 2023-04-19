
    if check("the robot's gripper is not near the button"):
        robot.put("gripper near button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("down on button")