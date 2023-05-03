# Steps:
    #  1. Put gripper near the button
    #  2. Push gripper forward against the button
    # First, put the gripper near the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # Once the gripper is near the button, push it forward to press the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("forward aligned with the button")