# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    # 1. Put gripper above the coffee button
    # 2. Push down on the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.move_gripper("vertically aligned with the coffee button", close_gripper=True)
    # Now that the gripper is lined up with the button, push down on the button.
    if check("the robot's gripper is near the coffee button"):
        robot.move_gripper("almost vertically aligned with the coffee button")