# Steps:
    #  1. Put gripper vertically above the button
    #  2. Move gripper down to press the button
    # First, put the gripper vertically above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Move the gripper down to press the button.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not quite touching the button"):
        robot.move_gripper("touching the button")