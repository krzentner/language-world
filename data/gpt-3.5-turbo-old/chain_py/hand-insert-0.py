# Steps:
    #  1. Pick up the puck with the hand
    #  2. Move the hand to the target location
    #  3. Release the puck
    
    # First, make sure the hand is open and near the puck
    if check("the hand is not open and near the puck"):
        robot.open("hand")
        robot.move("hand to puck")
    
    # Once the hand is near the puck, close it to pick up the puck
    if check("the hand is near the puck and the hand is open"):
        robot.close("hand around puck")
    
    # Move the hand to the target location while carrying the puck
    if check("the hand is holding the puck and not at the target location"):
        robot.move("hand to goal")
    
    # Once the hand reaches the target location, release the puck by opening the hand
    if check("the hand is holding the puck and at the target location"):
        robot.open("hand")