
    # Steps:
    #  1. Put stick between thermos and goal
    #  2. Push thermos toward goal
    # First, the robot needs to move the stick roughly in between the thermos
    # and the goal.
    if check("the stick is not in between thermos and goal"):
        robot.move_gripper("in between thermos and goal")
    # Now that the stick is between the thermos and the goal, apply enough force
    # to the thermos to move it towards the goal.
    if check("the stick is in between thermos and goal"):
        robot.move_gripper("near the goal")