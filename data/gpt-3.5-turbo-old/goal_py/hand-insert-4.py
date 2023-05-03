# Steps:
    #  1. Move hand above the puck, open fingers
    #  2. Close fingers around puck
    #  3. Move hand to target location, open fingers
    # First, put the hand above the puck with fingers open.
    if check("the robot's hand is not above the puck"):
        robot.move_hand("above the puck", open_fingers=True)
    # If the hand is above the puck with fingers open, close the fingers around
    # the puck to pick it up.
    if check("the robot's hand is above the puck and the fingers are open"):
        robot.move_hand("around the puck", close_fingers=True)
    # Once the hand is around the puck, move it to the target location and open
    # the fingers to place it.
    if check("the robot's hand is around the puck"):
        robot.move_hand("above the target location", open_fingers=True)