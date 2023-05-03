# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move the gripper above the wall
    #  2. Move the gripper forward to the button
    #  3. Line up the gripper from above
    #  4. Push down on the button from the top
    # We need to move the gripper above the wall first.
    if check("the robot's gripper is not vertically aligned with the wall"):
        robot.move_gripper("vertically aligned with the wall")
    # Once the gripper is above the wall, move it forward towards the button.
    if check("the robot's gripper is above the wall and not near the button"):
        robot.move_gripper("near the button")
    # Now that the gripper is close to the button, line it up from above.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Finally, push down on the button from the top.
    if check("the robot's gripper is near the button and vertically aligned with the button"):
        robot.move_gripper("near the button", close_gripper=False)