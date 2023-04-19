
    # Steps:
    #  1. Put the stick against the thermos
    #  2. Move the stick to pull the thermos
    # We can't reach the thermos directly with the robot's gripper, so we should
    # use the stick to achieve this.
    if check("the stick is not against the thermos"):
        robot.drop_stick("the thermos")
    # As long as the stick is still close to the thermos, start pushing it away
    # from the thermos with the gripper to start moving it.
    if check("the stick is close to the thermos"):
        robot.move_gripper("away from the thermos")
    # As long as the stick is still close to the thermos and the thermos isn't
    # near the target location, move the stick to pull the thermos towards the
    # target.
    if check("the stick is close to the thermos and the thermos is not near target location"):
        robot.move_gripper("towards the target location")