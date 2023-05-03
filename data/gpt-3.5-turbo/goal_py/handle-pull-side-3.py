# Steps:
    #  1. Put gripper around the handle
    #  2. Pull the handle up from the side
    # We should put the gripper around the handle before we try to pull up on it.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can pull up on it from the side.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("upwards from the handle")