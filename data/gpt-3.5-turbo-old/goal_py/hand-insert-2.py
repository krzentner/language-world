# Steps:
    #  1. Put the hand above the puck
    #  2. Grab the puck with the hand
    #  3. Move the puck to the target location
    # First, put the hand above the puck.
    if check("the hand is not above the puck"):
        robot.move_hand("above the puck")
    # If the hand is roughly above the puck, grab the puck.
    if check("the hand is above the puck and the hand is not holding the puck"):
        robot.move_hand("around the puck", close_hand=True)
    # If the hand is holding the puck, move the hand to the target location.
    if check("the hand is holding the puck and the hand is not above the target location"):
        robot.move_hand("above the target location")