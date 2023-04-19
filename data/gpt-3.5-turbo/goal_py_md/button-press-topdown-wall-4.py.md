# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    #Steps:
    #  1. Position gripper above the button, accounting for the wall
    #  2. Move the gripper above the button
    #  3. Move the gripper down to press the button
    #  4. Move the gripper back up
    # To overcome the wall, position the robot's gripper slightly to the side of the button 
    # and then move it over the button. 
    if check("the robot's gripper is not near the side of the button"):
        robot.move_gripper("beside the button")
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # Once above the button, move the gripper down to press it, then move it back up.
    if check("the robot's gripper is not over the button"):
        robot.move_gripper("over the button", close_gripper=True)
    if check("the robot's gripper is not almost vertically aligned with the button"):
        robot.move_gripper("almost vertically aligned with the button")
    if check("the robot's gripper is over the button"):
        robot.move_gripper("vertically aligned with the button")
        robot.move_gripper("over the button", close_gripper=False)