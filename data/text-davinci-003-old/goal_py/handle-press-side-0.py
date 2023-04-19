
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # If the robot's gripper is not near the handle, move it to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the robot's gripper is near the handle, push down on it.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("forward aligned with the handle")