
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    #  3. Move left to avoid wall
    # We need to line up the gripper with the button from above.
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not close to the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up with the button, push down on the button
    # to press it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is almost near button"):
        robot.move_gripper("close to the button")
    # If the wall is close, move left to avoid it.
    if check("the robot's gripper is close to button and the robot's gripper is close to wall"):
        robot.move_gripper("left of the wall")