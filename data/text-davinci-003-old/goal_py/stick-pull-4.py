
    # Steps:
    #  1. Put the stick behind the thermos
    #  2. Pull the thermos with the stick
    # First, make sure the stick is behind the thermos.
    if check("the stick is not behind the thermos"):
        robot.move_gripper("behind the thermos")
    # Once the stick is behind the thermos, pull the thermos.
    if check("the stick is behind the thermos"):
        robot.move_gripper("towards the target location")