# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move("gripper above the button")
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.push("down on the button")