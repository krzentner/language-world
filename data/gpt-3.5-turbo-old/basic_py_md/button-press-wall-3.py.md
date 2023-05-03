# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is below the button"):
        robot.move("gripper to right of button")
    if check("the robot's gripper is near the button"):
        robot.slide("gripper up to button")
    if check("the robot's gripper is above the button"):
        robot.push("down on button")