# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is above button and open"):
        robot.drop("gripper onto button")
    if check("the robot's gripper is around button"):
        robot.close("gripper around button")
    if check("the robot's gripper is around button and almost touching the surface, and the button is not pressed"):
        robot.push("button down")