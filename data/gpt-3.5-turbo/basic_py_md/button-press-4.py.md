# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper in front of button")
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button forward")