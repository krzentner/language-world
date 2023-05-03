# Steps:
    #  1. Place hand over puck
    #  2. Pick up the puck with the hand
    #  3. Hold the puck and move hand to target location
    # We don't have a gripper in this scenario, so we'll be using the robot's hand.
    # First, place the open hand over the puck.
    if check("the robot's hand is not over the puck and the hand is open"):
        robot.move_hand("over the puck")
    # Close the hand around the puck.
    if check("the robot's hand is over the puck and the hand is open"):
        robot.move_hand("around the puck")
    # Move the hand with the puck to the target location.
    if check("the robot's hand is holding the puck and is not near the target location"):
        robot.move_hand("near the target location")