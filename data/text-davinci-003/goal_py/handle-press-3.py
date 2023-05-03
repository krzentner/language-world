
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # If the gripper isn't close to the handle, we should move the gripper near
    # the handle to start pushing.
    if check("the robot's gripper is not near handle"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle, just push down on it.
    if check("the robot's gripper is near handle"):
        robot.move_gripper("forward aligned with handle")