# Steps:
    #  1. Put gripper near the handle
    #  2. Push down the handle
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, we can push down on the handle.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("above the handle")