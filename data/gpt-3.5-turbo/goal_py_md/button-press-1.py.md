# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    # 1. Put gripper in front of the button
    # 2. Move gripper down onto the button
    # 3. Push button
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.move_gripper("near the button", close_gripper=True)
    if check("the robot's gripper is near the button"):
        robot.move_gripper("pushed the button")