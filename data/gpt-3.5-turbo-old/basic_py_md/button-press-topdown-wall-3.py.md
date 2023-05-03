# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
def button_press_topdown_wall(robot):
    if check("the robot is not facing the button"):
        robot.turn("towards button")
    if check("the robot's gripper is not above the button"):
        robot.move("gripper to above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")
    if check("the robot's gripper is touching the wall"):
        robot.move("gripper away from wall")
        robot.lift("gripper up")