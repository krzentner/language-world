    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the front
    # Because this is just a button press, we just need to line up the gripper
    # from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")