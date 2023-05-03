# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move gripper to the top corner of the wall
    #  2. Tilt the gripper to reach over the wall
    #  3. Line up the gripper as viewed from above
    #  4. Push down on the button from the top
    # Move the gripper to the top corner of the wall
    if check("the robot's gripper is not at the top corner of the wall"):
        robot.move_gripper("to the top corner of the wall")
    # Tilt the gripper to reach over the wall
    if check("the robot's gripper is not tilted to reach over the wall"):
        robot.tilt_gripper("to reach over the wall")
    # Line up the gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")