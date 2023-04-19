# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    #  3. Release the button
    # First, put the gripper above the coffee machine button.
    if check("the robot's gripper is not vertically aligned with coffee machine button"):
        robot.move_gripper("vertically aligned with the coffee machine button")
    # If the robot's gripper is above the button, push down the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("pressing the button")
    # Release the button by opening the gripper.
    if check("the robot's gripper is pressing the button"):
        robot.move_gripper("vertically aligned with the coffee machine button", close_gripper=False)