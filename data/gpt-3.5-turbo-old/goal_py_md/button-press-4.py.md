# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Put gripper in front of button
    #  2. Lower gripper onto button
    #  3. Push down on the button
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button")
    # If the gripper is in front of the button, lower it onto the button.
    if check("the robot's gripper is in front of the button and the robot's gripper is not near the button"):
        robot.move_gripper("over the button", close_gripper=True)
    # Once the gripper is closed around the button, push down on the button.
    if check("the robot's gripper is near the button and the gripper is holding the button"):
        robot.move_gripper("pressed on the button")