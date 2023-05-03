
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on the button
    # First, put the gripper above the button.
    # We don't need to be precise here, because the button is much larger than
    # the robot's gripper.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # If the gripper is above the button, just push down on it.
    if check("the robot's gripper is above button"):
        robot.move_gripper("near the button", close_gripper=True)