# Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial in the correct direction
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Determine which direction to turn the dial.
    # Our strategy is to find the closest direction (left or right) to turn the dial.
    # If the correct direction is left, we want to turn the dial counter-clockwise.
    # If the correct direction is right, we want to turn the dial clockwise.
    dial_direction = determine_dial_direction()
    if dial_direction == "left":
        if check("the robot's gripper is not turned counter-clockwise"):
            robot.move_gripper("turned counter-clockwise")
    elif dial_direction == "right":
        if check("the robot's gripper is not turned clockwise"):
            robot.move_gripper("turned clockwise")