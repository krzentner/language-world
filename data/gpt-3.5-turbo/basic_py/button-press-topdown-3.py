if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not almost touching the button"):
        robot.move("gripper down to button")
    if check("the robot's gripper is almost touching the button"):
        robot.push("button down")