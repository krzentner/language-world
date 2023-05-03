# Steps:
    #  1. Put gripper above button
    #  2. Push gripper straight down onto the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is above the button, we can just push it straight down onto
    # the button.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not pushing down on button"):
        robot.move_gripper("pushing down on the button")