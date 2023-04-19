
    # Steps:
    #  1. Put gripper in front of button
    #  2. Push button
    # To press the button, the gripper needs to be in front of it and lined up
    # correctly.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # If the gripper is in front and lined up, just push.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")