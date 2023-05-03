# Steps:
    #  1. Put gripper around the handle
    #  2. Pull up the handle
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just pull up on it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("vertically aligned with the handle")