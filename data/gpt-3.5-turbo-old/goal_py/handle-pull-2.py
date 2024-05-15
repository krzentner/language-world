# Steps:
    # 1. Put gripper around the handle
    # 2. Pull up on the handle
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, just pull up on it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")