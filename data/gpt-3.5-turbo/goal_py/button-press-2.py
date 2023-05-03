# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put the gripper in front of the button
    #  2. Push gripper into the button
    #  3. Push down on the button
    # Because this is "front", we just need to line up the gripper from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not in front of button"):
        robot.move_gripper("in front of the button")
    # Now that the gripper is lined up, just push into the button to press it.
    if check("the robot's gripper is in front of the button and near the button"):
        robot.move_gripper("pressing the button")