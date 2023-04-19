
    # Steps:
    #  1. Put stick behind thermos
    #  2. Push the stick against the thermos
    #  3. Slide the thermos to the target location
    # First, put the stick behind the thermos.
    if check("the stick is not behind the thermos"):
        robot.move_gripper("behind the thermos")
    # If the stick is behind the thermos, we can start pushing it.
    if check("the stick is behind the thermos"):
        robot.move_gripper("near the thermos")
    # If the the stick is pushing the thermos, we can slide the thermos to the
    # target location.
    if check("the stick is pushing the thermos"):
        robot.move_gripper("near the target location")