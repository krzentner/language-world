# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button")