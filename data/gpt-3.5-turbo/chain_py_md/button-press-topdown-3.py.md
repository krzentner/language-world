# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down onto button
    #  3. Press down on button
    # Put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper is above the button, push it down onto the button.
    if check("the robot's gripper is above button, and the robot's gripper is not pressing down on the button"):
        robot.push("gripper down onto button")
    # Press down on the button.
    if check("the robot's gripper is pressing down on the button"):
        robot.press("down on button")