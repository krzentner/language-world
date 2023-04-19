# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper with the button
    #  2. Push the button from the front
    # Line up the robot's gripper with the button
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is behind the button, push the button from the front
    if check("the robot's gripper is behind the button"):
        robot.move_gripper("near the button")