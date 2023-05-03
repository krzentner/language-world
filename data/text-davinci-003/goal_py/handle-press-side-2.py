
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Push down the handle
    # Put the robot's gripper left of the handle to begin.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # As long as the gripper is still left of the handle, the robot can push down
    # the handle.
    if check("the robot's gripper is not left of the handle and the robot's gripper is near the handle"):
        robot.move_gripper("aligned with the handle")