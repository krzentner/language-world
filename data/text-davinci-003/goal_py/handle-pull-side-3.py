
    # Steps:
    #  1. Put gripper on left of the handle
    #  2. Pull up on the handle
    # First, we need to put the gripper left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle", close_gripper=True)
    # As long as the handle is still to the left, we can pull it up.
    if check("the robot's gripper is left of the handle and the robot's gripper is near the handle"):
        robot.move_gripper("above the handle")