# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # The coffee machine button is just like the button in button_press_topdown, except
    # it's probably a little larger, and may require a bit more force.
    # Line up the robot's gripper above the button, just like we did for button_press_topdown.
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move_gripper("vertically aligned with the coffee machine button", close_gripper=True)
    # Now that the gripper is lined up, we can press down on the button. 
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.move_gripper("near the coffee machine button", force=10)