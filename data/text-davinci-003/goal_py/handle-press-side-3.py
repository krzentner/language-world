
    # Steps:
    #  1. Line up gripper from side
    #  2. Push handle down from side
    # First, line up the gripper from the side.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle")
    # Once the robot's gripper is lined up, we can just push down on the handle
    # to press it.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.move_gripper("below the handle")