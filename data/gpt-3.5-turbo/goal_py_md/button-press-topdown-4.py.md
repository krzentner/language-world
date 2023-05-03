# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down to press button
    # The button can be pressed by trapping it with the gripper and pushing the
    # gripper down.
    # If the gripper isn't above the button, move it there.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Close the gripper to trap the button.
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is above the button and closed, push it down to press the button.
    if check("the robot's gripper is above the button and the robot's gripper is closed"):
        robot.move_gripper("above the button", closed_gripper=True, move_down=True)