# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper roughly above the button
    #  2. Move gripper down to button and grab it
    #  3. Push button down
    # First, put the gripper roughly above the button
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the gripper is not around the button, move it down and grab it
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.move_gripper("near the button", close_gripper=True)
    # Push the button down
    if check("the robot's gripper is around the button"):
        robot.move_gripper("near the button")