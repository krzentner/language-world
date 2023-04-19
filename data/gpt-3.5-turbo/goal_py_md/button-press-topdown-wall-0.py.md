# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move the gripper to the left of the button and close the gripper
    #  2. Move the gripper above the button and the short wall
    #  3. Open the gripper to pass the short wall
    #  4. Push down on the button from above
    # Move the gripper to the left of the button and close the gripper
    if check("the robot's gripper is not left of the button"):
        robot.move_gripper("left of the button", close_gripper=True)
    # Move the gripper to be above the button and the short wall
    if check("the robot's gripper is not vertically aligned with the button and is not above the short wall"):
        robot.move_gripper("above the button and the short wall")
    # Open the gripper to pass the short wall
    if check("the robot's gripper is not open"):
        robot.move_gripper("above the button")
    # Push down on the button from above
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")