if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not touching the button"):
        robot.push("button top-down")