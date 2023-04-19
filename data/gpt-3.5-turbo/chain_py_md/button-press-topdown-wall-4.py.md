# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move the gripper to be near the button and short wall
    #  2. Put gripper above the button from a distance by raising the height
    #  3. Lower the gripper with appropriate orientation so that it is holding the button
    #  4. Rotate the gripper to press the button from above
    #  5. Push down on the button

    # First, move the gripper so that it's near the button
    if check("the robot's gripper is not near the button and the short wall that's blocking it"):
        robot.move("gripper to the right of the button and the short wall")
    # Position the gripper above the button from a distance by raising the height
    if check("the robot's gripper is not above the button and the robot's gripper is not almost vertically aligned with button"):
        robot.raise_height("gripper above button")
    # Move the gripper down with the appropriate orientation so that it's holding the button
    if check("the robot's gripper is above the button and the robot's gripper is not holding the button"):
        robot.lower_gripper("with the correct orientation")
    # Rotate the gripper to press the button from above
    if check("the robot's gripper is holding the button and it's not rotated to press down on it"):
        robot.rotate_gripper("to the correct angle")
    # Push down on the button
    if check("the robot's gripper is holding the button and is positioned to press down on it"):
        robot.push("down on the button")