if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.move("gripper to the side of button")
    if check("the robot's gripper is near the button"):
        robot.push("button down")