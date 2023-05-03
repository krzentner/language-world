# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down onto button
    # We need to put the gripper roughly above the button before we can push it.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Once the gripper is lined up above the button, we can push the button down
    # by moving the gripper forward and down onto the button.
    if check("the robot's gripper is above button"):
        robot.move_gripper("on the button")