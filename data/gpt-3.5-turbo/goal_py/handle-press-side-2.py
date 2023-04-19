# Steps:
    #  1. Put gripper around the handle
    #  2. Push down on the handle from the side
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, we can push down on it from the side.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the top of the handle")