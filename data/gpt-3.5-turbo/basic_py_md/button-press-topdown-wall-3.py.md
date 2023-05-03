# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to above the button")
    if check("the robot's gripper is above the button and not too close to the wall"):
        robot.push("down on button")
    if check("the robot's gripper is too close to the wall"):
        robot.move("gripper to the side of the button and away from the wall")
        robot.push("down on button")