# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down onto button
    #  3. Push the button down
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to press it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near button"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is near the button, we've probably pressed it enough.
    # Move the gripper back up.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("vertically aligned with the button")