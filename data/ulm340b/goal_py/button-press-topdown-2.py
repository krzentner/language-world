
    # Steps:
    #  1. Put gripper above the button
    #  2. Move down to push the button
    # To press a button, we can move the gripper down right above the button,
    # causing the gripper to close.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("around the button", close_gripper=True)

# door-close: push the door close
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from the front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("right of the door handle")

# button-press-side: push the button in sideways
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Move down to push the button
    # To press a button, we can move the gripper down right above the button,
    # causing the gripper to close.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # As long as the gripper is aligned with the button, we can just move it
    # down to press the button.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button", close_gripper=True)

# button-press-down: push the button down from the side
def button_press_down(robot):
    # Steps:
    #  1. Put gripper above the button
    #  