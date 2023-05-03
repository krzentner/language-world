if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not above button"):
        robot.push("gripper down to button")
    if check("the robot's gripper is above the button and the robot's gripper is touching the button"):
        robot.push("button down")