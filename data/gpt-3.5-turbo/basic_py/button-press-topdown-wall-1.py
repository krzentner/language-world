if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not behind wall"):
        robot.move("gripper behind wall")
    if check("the robot's gripper is behind wall"):
        robot.push("down on button")