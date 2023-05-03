
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper to the button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is open"):
        robot.close("gripper around button")
    if check("the robot's gripper is near button"):
        robot.push("down on button")