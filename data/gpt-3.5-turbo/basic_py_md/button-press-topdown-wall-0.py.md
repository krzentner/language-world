# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not on the left of the wall"):
        robot.move("gripper to left of wall")
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")