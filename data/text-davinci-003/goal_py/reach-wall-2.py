
    # Steps:
    #  1. Reach towards the target
    #  2. Move up and around the wall
    # First, reach towards the target to get as close as possible.
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")
    # If the robot sees the wall, move up and around the wall to the target
    # location.
    if check("the robot's gripper is horizontally aligned with wall"):
        robot.move_gripper("above the reach target")