# Steps:
    #  1. Put hand above the puck
    #  2. Use fingers to grab the puck
    #  3. Move hand to target location
    #  4. Use fingers to release the puck
    # Use the same logic as in pick_place() to first put the hand above the puck.
    if check("the robot's hand is not above the puck"):
        robot.move_hand("above the puck")
    # If the hand isn't grabing the puck, use the fingers to grab it.
    if check("the robot's hand is not grabbing the puck"):
        robot.grab_puck()
    # Move the hand to the target location. We can use similar logic as in reach().
    if check("the robot's hand is not near target location"):
        robot.move_hand("near the target location")
    # Release the puck by opening the fingers.
    if check("the robot's hand is grabbing the puck and the hand is near the target location"):
        robot.release_puck()