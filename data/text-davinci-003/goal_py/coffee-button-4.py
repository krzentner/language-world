
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # To button buttons, it's usually easiest if the gripper is directly
    # (i.e. "over") the button on the surface it's pressed.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # When in that position, push the gripper down onto the button.
    if check("the robot's gripper is above button and the robot's gripper is not near button"):
        robot.move_gripper("near the button")