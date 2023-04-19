
    if check("the robot's gripper is below the button"):
        robot.put("gripper above the button")
    if check("the robot's gripper is above the button"):
        robot.push("down on the button")