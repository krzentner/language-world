
    # Steps:
    #  1. Put gripper above the button
    #  2. Press the button
    # Put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the gripper isn't near the button, move it into the button.
    if check("the robot's gripper is not near button"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is near the button, push down on the button.
    if check("the robot's gripper is near button"):
        robot.move_gripper("down")