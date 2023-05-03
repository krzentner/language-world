# Steps:
    #  1. Put gripper slightly above button
    #  2. Move gripper down onto button
    #  3. Press button down
    # First, put the gripper just above the button so that it doesn't hit it
    # while trying to press it.
    if check("the robot's gripper is not slightly above the button"):
        robot.move_gripper("slightly above the button")
    # Once the gripper is slightly above the button, move it down onto the
    # button.
    if check("the robot's gripper is above the button and the robot's gripper is not touching the button"):
        robot.move_gripper("touching the button")
    # Finally, press the button down by closing the gripper.
    if check("the robot's gripper is touching the button and the robot's gripper is open"):
        robot.move_gripper("touching the button and holding it down")