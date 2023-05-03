# Steps:
    #  1. Put gripper above button
    #  2. Push down on the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.move_gripper("above the coffee machine button")
    # Now that the gripper is above the button, just push down on it to start
    # the coffee machine.
    if check("the robot's gripper is above the coffee machine button"):
        robot.move_gripper("near the coffee machine button")