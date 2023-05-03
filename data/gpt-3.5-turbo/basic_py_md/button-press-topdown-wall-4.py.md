# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not aligned with the button and the robot's gripper is not aligned with the wall"):
        robot.move("gripper above button")
    if check("the robot's gripper is aligned with the button and the robot's gripper is not closed"):
        robot.close("gripper around button")
    if check("the robot's gripper is closed and the robot's gripper is above the wall and the button is not pressed"):
        robot.push("down on button")
    if check("the button is pressed"):
        robot.move("gripper up and away from button")