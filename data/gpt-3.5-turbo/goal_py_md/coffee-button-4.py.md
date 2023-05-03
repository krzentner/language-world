# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Move gripper above the coffee button
    #  2. Push down on the button
    # First, we need to position the gripper above the coffee button.
    if check("the robot's gripper is not above the coffee button"):
        robot.move_gripper("above the coffee button")
    # Once the gripper is above the button, we can push down on it.
    if check("the robot's gripper is above the coffee button"):
        robot.move_gripper("on the coffee button", close_gripper=True)