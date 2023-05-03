# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not in front of the button and the wall is between the robot and the button"):
        robot.move("gripper to the right of the wall and then in front of the button")
    if check("the robot's gripper is in front of the button and the wall is between the robot and the button"):
        robot.push("button forward")