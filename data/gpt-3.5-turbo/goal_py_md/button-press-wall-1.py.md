# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Move gripper to the left of the wall
    #  2. Move gripper forward to the button
    #  3. Push down on the button
    # If the gripper is not to the left of the wall, move it there.
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # If the gripper is left of the wall but not forward to the button, move it there.
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is left of the button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Finally, push down on the button to activate it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")