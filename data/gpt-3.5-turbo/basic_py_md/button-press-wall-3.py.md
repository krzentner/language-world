# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    if check("the robot's gripper is not in front of the button and the robot's gripper is not near the button"):
        robot.move("gripper to front of button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not near the wall"):
        robot.move("gripper to near the wall in front of button")
    if check("the robot's gripper is near the wall"):
        robot.slide("the gripper along the wall towards the button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("button forward")