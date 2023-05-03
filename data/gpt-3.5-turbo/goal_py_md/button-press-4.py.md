# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Move the gripper forward to push the button
    #  3. Release the button
    # First, we need to move the gripper to a position in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button")
    # Next, we need to move the gripper forward to push the button.
    if check("the robot's gripper is in front of the button and the robot's gripper is not close to the button"):
        robot.move_gripper("close to the button", close_gripper=True)
    # Finally, we need to release the button by opening the gripper again.
    if check("the robot's gripper is close to the button"):
        robot.move_gripper("in front of the button", close_gripper=False)