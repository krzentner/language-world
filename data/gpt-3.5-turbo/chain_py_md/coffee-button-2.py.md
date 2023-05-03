# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # We'll assume that the robot is already in front of the coffee machine.
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.place("gripper above coffee machine button")
    # Once the gripper is above the button, push down on it to start the coffee.
    if check("the robot's gripper is above the coffee machine button"):
        robot.push("down on coffee machine button")