# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and is not blocked by the short wall"):
        robot.push("down on button")
    if check("the robot's gripper is blocked by the short wall and the short wall is between the robot and the button"):
        robot.move("the gripper to the left of the wall")
        robot.move("the gripper in front of the wall")
        robot.slide("the gripper over the wall")
        robot.move("the gripper in front of the button")
        robot.push("down on button")