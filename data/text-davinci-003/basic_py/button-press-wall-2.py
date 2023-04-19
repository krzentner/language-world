
    if check("the robot's gripper is not open and the robot's gripper is not vertically aligned with wall"):
        robot.put("gripper in front of wall")
    if check("the robot's gripper is vertically aligned with wall"):
        robot.open("gripper")
    if check("the robot's gripper is open and the robot's gripper is not behind the wall and the robot's gripper is not in front of the button"):
        robot.move("gripper behind wall")
    if check("the robot's gripper is in front of the button"):
        robot.push("button")