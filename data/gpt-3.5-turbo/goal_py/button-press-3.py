# Steps:
    #  1. Put the gripper in front of the button
    #  2. Push the button
    # Position the robot's gripper in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button", close_gripper=True)
    # Push the button by moving the gripper forward.
    if check("the robot's gripper is in front of the button"):
        robot.move_gripper("near the button")