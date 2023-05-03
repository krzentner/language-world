# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move to the side of the wall opposite the button
    #  2. Put the gripper above the button
    #  3. Move the wall away
    #  4. Push down on the button
    # Move to the side of the wall opposite the button.
    if check("the robot is not on the opposite side of the wall from the button"):
        robot.move("to opposite side of wall from button")
    # Put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Move the wall away.
    if check("the wall is not moved away"):
        robot.move("wall away")
    # Push down on the button.
    if check("the robot's gripper is vertically aligned with and above button"):
        robot.push("down on button")