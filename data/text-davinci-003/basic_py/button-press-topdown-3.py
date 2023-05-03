
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is far from button"):
        robot.move("gripper closer to button")
    if check("the robot's gripper is near the button"):
        robot.push("down the top of button")