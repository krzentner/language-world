
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")