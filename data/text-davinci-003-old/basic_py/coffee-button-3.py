
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("the gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")