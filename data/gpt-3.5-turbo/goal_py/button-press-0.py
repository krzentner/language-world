# Steps:
    #  1. Line up the gripper from the front
    #  2. Push the button in
    # First, line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push in on the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")