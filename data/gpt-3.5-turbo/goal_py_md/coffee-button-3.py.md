# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Move the gripper above the coffee button
    #  2. Push down on the button
    # First, put the gripper above the coffee button.
    if check("the robot's gripper is not above the coffee button"):
        robot.move_gripper("above the coffee button")
    # If the gripper is above the coffee button, push the button.
    if check("the robot's gripper is above the coffee button"):
        robot.move_gripper("near the coffee button")