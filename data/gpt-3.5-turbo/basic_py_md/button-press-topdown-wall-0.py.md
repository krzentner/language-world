# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above the button and the robot's gripper is not behind the wall"):
        robot.move("gripper behind the wall")
    if check("the robot's gripper is behind the wall and the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper to side of button")
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")