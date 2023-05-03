# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Position gripper above button
    #  2. Move gripper to right of the button and close
    #  3. Move gripper upwards and over the wall
    #  4. Move gripper back down to top of button
    #  5. Push down on the button

    # Put the gripper vertically aligned with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with button", close_gripper=True)
    # Move the gripper to the right of the button and close it
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not right of the button"):
        robot.move_gripper("right of the button", close_gripper=True)

    # Move the gripper up and over the wall
    if check("the robot's gripper is right of the button"):
        robot.move_gripper("above the wall")

    # Move the gripper back down to the top of the button
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("vertically aligned with button")

    # Push down on the button
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button", close_gripper=False)