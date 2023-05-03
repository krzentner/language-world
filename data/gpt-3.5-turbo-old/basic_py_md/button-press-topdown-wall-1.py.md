# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to the wall")
    if check("the robot's gripper is near the wall"):
        robot.push("gripper against the wall")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")