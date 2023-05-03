# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    if check("the robot's gripper is not aligned with the button and there is a wall in front of the robot"):
        robot.move("gripper to the left of the button")
    if check("the robot's gripper is aligned with the button and there is a wall in front of the robot"):
        robot.move("gripper forward to the button")
        robot.push("button down")
    if check("the button is pressed"):
        robot.move("gripper backward")
        robot.move("gripper to the right of the button")