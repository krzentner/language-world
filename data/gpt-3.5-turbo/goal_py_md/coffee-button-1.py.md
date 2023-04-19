# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the coffee machine button
    #  2. Push down on the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move_gripper("vertically aligned with the coffee machine button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.move_gripper("near the coffee machine button")