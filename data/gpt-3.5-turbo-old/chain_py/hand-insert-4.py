# Steps:
    #  1. Use hand to pick up the puck
    #  2. Carry the puck to the goal location
    #  3. Release the puck at the goal location
    # First, use the hand to pick up the puck.
    if check("the robot's hand is not holding the puck"):
        robot.pick_up("puck with hand")
    # If the hand is holding the puck, carry it to the goal location.
    if check("the robot's hand is holding the puck and the hand is not near the goal location"):
        robot.move("hand with puck to goal location")
    # If the hand is near the goal location, release the puck.
    if check("the robot's hand is holding the puck and the hand is near the goal location"):
        robot.release("puck at goal location")