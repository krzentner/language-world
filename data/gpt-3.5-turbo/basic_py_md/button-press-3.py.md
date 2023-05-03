# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("button")