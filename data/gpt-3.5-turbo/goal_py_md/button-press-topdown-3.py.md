# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the gripper down onto the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the gripper isn't close to the button, move it down towards the button.
    if check("the robot's gripper is above the button and the robot's gripper is not near the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the gripper is near the button, push the gripper down onto the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("close to the surface of the button")