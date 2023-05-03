# Steps:
    #  1. Put hand near puck
    #  2. Wrap fingers around puck
    #  3. Lift puck
    #  4. Move hand to goal
    # We're picking up the puck with the hand this time, so we need to
    # adjust the movement accordingly.
    # Move the hand close to the puck.
    if check("the robot's hand is not near the puck"):
        robot.move_hand("near the puck")
    # Once the hand is near the puck, close the fingers around the puck to
    # pick it up.
    if check("the robot's hand is near the puck and the robot's fingers are not wrapped around the puck"):
        robot.move_hand("wrapped around the puck")
    # Now that the hand has the puck, move it to the target location.
    if check("the robot's fingers are wrapped around the puck and the robot's hand is not near the goal"):
        robot.move_hand("near the goal")