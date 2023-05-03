# Steps:
    #  1. Pick up the puck with the hand
    #  2. Move the hand to the target location
    # We're using a hand for this, so we won't have a gripper to open and close.
    # If the puck isn't below the hand, move it above the puck.
    if check("the robot's hand is not above the puck"):
        robot.move_hand("above the puck")
    # If the hand is above the puck, move it down to pick up the puck.
    if check("the robot's hand is above the puck"):
        robot.move_hand("around the puck")
    # If the hand is around the puck, move it to the target location.
    if check("the robot's hand is holding the puck and the hand is not near the target location"):
        robot.move_hand("near the target location")