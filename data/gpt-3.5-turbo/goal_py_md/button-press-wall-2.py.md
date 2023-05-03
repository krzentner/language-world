# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Move gripper to a position in front of the button and above the wall
    #  2. Move gripper down to press the button
    #  3. Move gripper back up
    # In this task, there is a short wall in front of the button, so we need to
    # move the gripper to a position above the wall in order to press the button.
    # Move the gripper to a position above the wall and in front of the button.
    if check("the robot's gripper is not above the wall and in front of the button"):
        robot.move_gripper("above the wall and in front of the button")
    # Move the gripper down to press the button.
    if check("the robot's gripper is above the button and not pressing down"):
        robot.move_gripper("on top of the button", close_gripper=True)
    # Move the gripper back up.
    if check("the robot's gripper is pressing down on the button"):
        robot.move_gripper("above the wall and in front of the button")