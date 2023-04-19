
    # Steps:
    #  1. Put gripper near button
    #  2. Push button
    # Start by moving the robot's gripper near the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # If the gripper is near the button, we can just press it.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("vertically aligned with the button")