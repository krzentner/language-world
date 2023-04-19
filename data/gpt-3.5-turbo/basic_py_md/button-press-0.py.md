# button-press: push the button from the front
# def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with the button and the robot's gripper is not near the button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is near the button"):
        robot.push("button")