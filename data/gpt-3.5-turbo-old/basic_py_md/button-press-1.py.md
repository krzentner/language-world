# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to the front of the button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not around the button"):
        robot.grab("the button")
    if check("the robot's gripper is around the button"):
        robot.push("down on the button")