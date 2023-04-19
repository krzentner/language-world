
    # Steps:
    #  1. Put stick against the thermos
    #  2. Pull the thermos to the target location
    # First, move the stick close to the thermos.
    if check("the stick is not near the thermos"):
        robot.move_gripper("near the thermos")
    # If the stick is close to the thermoses, we can use it to pull the
    # thermos to the target location.
    # Move the stick away in the direction of the target location.
    if check("the stick is near the thermos"):
        robot.move_gripper("away from the thermos towards the target location")