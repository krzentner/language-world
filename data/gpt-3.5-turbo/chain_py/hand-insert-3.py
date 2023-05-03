# Steps:
    #  1. Put hand near the puck
    #  2. Grab the puck with the hand
    #  3. Move the puck to the goal
    # Because we're using a hand instead of a gripper, we don't need to worry
    # about lining up or opening/closing the gripper.
    # First, move the hand close to the puck.
    if check("the robot's hand is not near the puck"):
        robot.move("hand near puck")
    # Grab the puck with the hand.
    if check("the robot's hand is near the puck"):
        robot.grab("puck")
    # Move the puck to the goal.
    if check("the robot's hand is holding the puck"):
        robot.move("puck to goal")