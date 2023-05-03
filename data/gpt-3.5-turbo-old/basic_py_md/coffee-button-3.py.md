# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
def coffee_button(robot):
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move("gripper to right of coffee machine button")
    if check("the robot's gripper is near the coffee machine button"):
        robot.push("down on coffee machine button")