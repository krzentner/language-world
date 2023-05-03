
    # Steps:
    #  1. Put the stick beneath the thermos
    #  2. Move robot and stick in the direction of goal
    # First, put the stick beneath the thermos.
    if check("the stick is not below the thermos"):
        robot.put("stick beneath the thermos")
    # Now that the stick is beneath the thermos, we can pull the thermos by
    # moving the robot and stick in the direction of goal.
    if check("the stick is below the thermos"):
        robot.move("robot and stick in direction of goal")