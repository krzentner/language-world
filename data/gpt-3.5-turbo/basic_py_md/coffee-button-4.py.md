# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot's gripper is not near the coffee machine button"):
        robot.reach("the coffee machine button")
    if check("the robot's gripper is near the coffee machine button and the robot's gripper is not touching the button"):
        robot.push("down on coffee machine button")