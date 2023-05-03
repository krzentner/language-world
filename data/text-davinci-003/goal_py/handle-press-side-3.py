
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # Only need to move the robot's gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, just push down on it from the side.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("vertically aligned with the handle")