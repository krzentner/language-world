
    # Steps:
    #  1. Put gripper near the button
    #  2. Push down on the button
    # If the robot's gripper is not near the coffee machine button, move it to
    # the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # If the gripper is near the coffee machine button, push the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button")