# Steps:
    #  1. Put hand over the puck
    #  2. Move hand to target location while holding the puck
    # Since we don't have a gripper, we'll use the robot's hand to grab and move
    # the puck.
    # First, put the hand over the puck.
    if check("the robot's hand is not above the puck"):
        robot.move_hand("above the puck")
    # If the hand isn't grasping the puck, grasp it.
    if check("the robot's hand is not grasping the puck"):
        robot.move_hand("around the puck")
    # If the puck is grasped, move the hand to the target location.
    if check("the robot's hand is grasping the puck and the robot's hand is not near the target location"):
        robot.move_hand("near the target location", grasp_puck=True)