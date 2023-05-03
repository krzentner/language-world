if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not on the button"):
        robot.push("gripper down onto button")
    if check("the robot's gripper is on the button"):
        robot.push("button down")