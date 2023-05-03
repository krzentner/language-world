# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot is not in front of the coffee machine and the robot's gripper is not near the button"):
        robot.move("to coffee machine")
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")