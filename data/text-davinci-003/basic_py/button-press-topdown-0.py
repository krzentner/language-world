
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not almost touching button"):
        robot.put("gripper near button")
    if check("the robot's gripper is almost touching button"):
        robot.push("down on button")