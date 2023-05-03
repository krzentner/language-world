# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot's gripper is not above the coffee machine button"):
        robot.place("gripper above coffee machine button")
    if check("the robot's gripper is open"):
        robot.drop("gripper around coffee machine button")
    if check("the robot's gripper is near the coffee machine button and the robot's gripper is open"):
        robot.close("gripper around coffee machine button")
    if check("the robot's gripper is above the coffee machine button and the robot's gripper is closed"):
        robot.push("down on coffee machine button")