
    # Steps:
    #  1. Put gripper right of the handle
    #  2. Push the handle down
    # First, put the gripper near the handle.
    if check("the robot's gripper is not right of the handle"):
        robot.move_gripper("right of the handle")
    # Now just push down on the handle.
    if check("the robot's gripper is right of the handle"):
        robot.move_gripper("left of the handle")