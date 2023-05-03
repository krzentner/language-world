
    # Steps:
    #  1. Line up gripper as viewed from side
    #  2. Push side of button
    # When pushing the button, we don't need to be perfectly lined up, since the
    # button is likely larger than the gripper.
    # We just need to roughly line up the gripper from the side.
    if check("the robot's gripper is not almost above the button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Now that the gripper is roughly lined up, just push the side of the button.
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.move_gripper("above the button")