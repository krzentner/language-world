
    # Steps:
    #  1. Reach the hand
    #  2. Put the hand over the puck
    #  3. Insert the hand
    #  4. Move the hand with the puck to the goal
    # Much like pick-place, but with a hand.
    # First, reach the hand.
    if check("the robot's hand is not near target"):
        robot.reach("hand")
    # Put the hand over the puck.
    if check("the robot's hand is not over puck"):
        robot.put("hand over puck")
    # Insert the hand.
    if check("the robot's hand is not around puck"):
        robot.insert("hand into puck")
    # Move the hand with the puck to the target location.
    if check("the robot's hand is around the puck"):
        robot.move("hand with puck to goal")