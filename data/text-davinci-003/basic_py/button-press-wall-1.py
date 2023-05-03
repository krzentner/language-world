
    if check("the robot's gripper is not above the wall and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper near top of wall")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")