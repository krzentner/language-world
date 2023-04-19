# Steps:
    #  1. Pick up the puck with your hand
    #  2. Move your hand to the target location
    # Since we're using our hand instead of a gripper, we don't need to worry
    # about the orientation of the object or the gripper.
    # First, use your hand to pick up the puck.
    if check("the puck is not in your hand"):
        robot.pickup("the puck")
    # Once the puck is in your hand, move your hand to the target location.
    if check("the puck is in your hand and your hand is not at the target location"):
        robot.move("your hand to the goal")