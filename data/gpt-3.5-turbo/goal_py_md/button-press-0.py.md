# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Move the gripper towards the button until it presses it
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Once the gripper is lined up in front of the button, move it towards the
    # button until it presses it.
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.move_gripper("near the button")