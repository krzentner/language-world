
    # Steps:
    #  1. Put the gripper in front of the button
    #  2. Push the button
    # If the gripper is not forward aligned with the button, we just need to
    # position the gripper in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Once the gripper is forward aligned with the button, just push down on it.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")