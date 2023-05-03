# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above coffee machine button
    #  2. Push down on the button
    # First, put the gripper above the coffee machine button.
    if check("the robot's gripper is not above coffee machine button"):
        robot.put("gripper above coffee machine button")
    # If the gripper is above the button, push down on it.
    if check("the robot's gripper is above coffee machine button"):
        robot.push("down on button")