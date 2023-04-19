
    # Steps:
    #  1. Put gripper in front of button
    #  2. Push button
    # If the gripper is not in front of the button, move it in front of the
    # button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Now that the gripper is in front of the button, push it.
    if check("the robot's gripper is forwards aligned with button"):
        robot.move_gripper("vertically aligned with the button")