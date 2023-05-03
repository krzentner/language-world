
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper left of button")
    if check("the robot's gripper is below button"):
        robot.put("gripper above button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button")