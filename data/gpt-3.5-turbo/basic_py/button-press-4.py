if check("the robot's gripper is not almost horizontally aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is almost horizontally aligned with button"):
        robot.push("button")