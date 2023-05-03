
    # Steps:
    #  1. Put gripper horizontally aligned with handle
    #  2. Push down on the handle
    # First, move the gripper to the side of the handle.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.move_gripper("horizontally aligned with handle", close_gripper=True)
    # When the gripper is lined up, push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.move_gripper("forward aligned with the handle")