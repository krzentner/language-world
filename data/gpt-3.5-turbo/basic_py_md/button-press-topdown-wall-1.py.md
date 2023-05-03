# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
    if check("there is a wall between the robot's gripper and the button"):
        robot.move("gripper left")
        robot.move("gripper down")
        robot.move("gripper right")
        robot.push("down on button")