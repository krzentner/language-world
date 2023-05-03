# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not near the button and the robot's gripper is not blocked by the wall"):
        robot.move("front of the button")
    if check("the robot's gripper is in front of the button"):
        robot.push("button")
    if check("the robot's gripper is blocked by the wall and the wall is short"):
        robot.move("to the side of the wall")
        robot.move("to the front of the button")
        robot.push("button")