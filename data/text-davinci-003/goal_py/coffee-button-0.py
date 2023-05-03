
    # Steps: 
    #  1. Line up the gripper as viewed from in front
    #  2. Push down on the button
    # Since this is for a button, line up the gripper from in front instead of
    # from above.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")