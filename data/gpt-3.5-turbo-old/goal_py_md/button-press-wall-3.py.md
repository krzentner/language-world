# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #   1. Move the gripper above the button and the wall
    #   2. Move the gripper forward to contact the wall
    #   3. Move the gripper down to the level of the button
    #   4. Push the button
    # First, move the gripper above the button and the short wall.
    if check("the robot's gripper is not vertically aligned with the button and wall"):
        robot.move_gripper("vertically aligned with the button and wall")
    # Once the gripper is above the button and the wall, move it forward to
    # contact the wall.
    if check("the robot's gripper is not in contact with the wall"):
        robot.move_gripper("in contact with the wall")
    # Now that the gripper is in contact with the wall, move it down to the
    # level of the button.
    if check("the robot's gripper is not at the level of the button"):
        robot.move_gripper("at the level of the button")
    # Finally, push the button.
    if check("the robot's gripper is not pushing the button"):
        robot.move_gripper("pushing the button")